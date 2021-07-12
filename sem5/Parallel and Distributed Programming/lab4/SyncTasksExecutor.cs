using System;
using System.Collections.Generic;
using System.Net;
using System.Net.Sockets;
using System.Text;
using System.Threading.Tasks;

namespace AsyncTasks
{
    public class SyncTasksHttpExecutor
    {
        private List<string> _hosts;
        private List<Task> _tasks;

        public SyncTasksHttpExecutor(List<string> hosts)
        {
            this._hosts = hosts;
            this._tasks = new List<Task>();
        }

        public void Execute()
        {
            for (var i = 0; i < _hosts.Count; i++)
            {
                _tasks.Add(Task.Factory.StartNew(Fetch, (_hosts[i], i)));
            }
            Task.WaitAll(_tasks.ToArray());
        }

        private static void Fetch(object args)
        {
            var host = ((ValueTuple<string, int>) args).Item1;
            var id = ((ValueTuple<string, int>) args).Item2;
            
            var ipHostInfo = Dns.GetHostEntry(host.Split('/')[0]);
            var ipAddr = ipHostInfo.AddressList[0];
            var remoteEndpoint = new IPEndPoint(ipAddr, HttpParser.Port);
            
            var clientSocket = new Socket(ipAddr.AddressFamily, SocketType.Stream, ProtocolType.Tcp);
            var requestWrapper = new RequestWrapper
            {
                Socket = clientSocket,
                Hostname = host.Split('/')[0],
                Endpoint = host.Contains("/") ? host.Substring(host.IndexOf("/", StringComparison.Ordinal)) : "/",
                RemoteEndPoint = remoteEndpoint,
                Id = id
            };

            ConnectWrapper(requestWrapper).Wait();
            SendWrapper(requestWrapper, HttpParser.GetRequestString(requestWrapper.Hostname, 
                requestWrapper.Endpoint)).Wait();
            ReceiveWrapper(requestWrapper).Wait();
            
            Console.WriteLine(
                "-- Client #{0} received {2} chars (headers + body), expected {1} chars in body", 
                id, HttpParser.GetContentLength(requestWrapper.ResponseContent.ToString()), requestWrapper.ResponseContent.Length);

            // release the socket
            clientSocket.Shutdown(SocketShutdown.Both);
            clientSocket.Close();
        }
        
        private static Task ConnectWrapper(RequestWrapper requestWrapper) {
            requestWrapper.Socket.BeginConnect(requestWrapper.RemoteEndPoint, ConnectCallback, requestWrapper);
            return Task.FromResult(requestWrapper.ConnectionFlag.WaitOne());  // blocks here
        }

        private static void ConnectCallback(IAsyncResult ar) {
            var requestWrapper = (RequestWrapper) ar.AsyncState;
            var clientSocket = requestWrapper.Socket;
            var clientId = requestWrapper.Id;
            var hostname = requestWrapper.Hostname;
            clientSocket.EndConnect(ar);

            Console.WriteLine("Client #{0}: Socket connected to {1} ({2})", clientId, hostname, clientSocket.RemoteEndPoint);
            
            requestWrapper?.ConnectionFlag.Set(); // signal that the connection has been made 
        }

        private static Task SendWrapper(RequestWrapper requestWrapper, string data) {
            var byteData = Encoding.ASCII.GetBytes(data);
            requestWrapper.Socket.BeginSend(byteData, 0, byteData.Length, 0, SendCallback, requestWrapper);
            return Task.FromResult(requestWrapper.SentFlag.WaitOne());  // blocks
        }

        private static void SendCallback(IAsyncResult ar) {
            var state = (RequestWrapper) ar.AsyncState;
            var clientSocket = state.Socket;
            var clientId = state.Id;
            var bytesSent = clientSocket.EndSend(ar);  // blocks until the message has been sent
            Console.WriteLine("Client #{0}: Sent {1} bytes to server.", clientId, bytesSent);
            
            state?.SentFlag.Set(); // signal that all bytes have been sent
        }

        private static Task ReceiveWrapper(RequestWrapper requestWrapper) {
            requestWrapper.Socket.BeginReceive(requestWrapper.Buffer, 0, RequestWrapper.BufferSize, 0, 
                ReceiveCallback, requestWrapper);
            return Task.FromResult(requestWrapper.ReceivedFlag.WaitOne());  // blocks
        }

        private static void ReceiveCallback(IAsyncResult ar) {
            var requestWrapper = (RequestWrapper) ar.AsyncState;
            var clientSocket = requestWrapper.Socket;

            try {
                var bytesRead = clientSocket.EndReceive(ar);  // blocks until a chunk of data has been received
                requestWrapper.ResponseContent.Append(Encoding.ASCII.GetString(requestWrapper.Buffer, 0, 
                    bytesRead));
                // if the response header has not been fully obtained, get the next chunk of data
                if (!HttpParser.ResponseHeaderObtained(requestWrapper.ResponseContent.ToString()))
                    clientSocket.BeginReceive(requestWrapper.Buffer, 0, RequestWrapper.BufferSize, 0, 
                        ReceiveCallback, requestWrapper);
                else
                {
                    // header has been fully obtained, so we get the body
                    var responseBody = HttpParser.GetResponseBody(requestWrapper.ResponseContent.ToString());
                    
                    if (responseBody.Length < HttpParser.GetContentLength(requestWrapper.ResponseContent.ToString()))
                    {
                        clientSocket.BeginReceive(requestWrapper.Buffer, 0, RequestWrapper.BufferSize, 0, 
                            ReceiveCallback, requestWrapper);
                    }
                    else
                    {
                        requestWrapper.ReceivedFlag.Set();
                    }
                }
            } catch (Exception e) {
                Console.WriteLine(e.ToString());
            }
        }
    }
}