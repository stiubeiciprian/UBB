using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Threading;

namespace AsyncTasks
{
    internal static class Program
    {
        private static void Main()
        {
            var hosts = new List<string> {"www.cs.ubbcluj.ro/", "google.com"};
            //var executor = new SyncTasksHttpExecutor(hosts);
            //var executor = new AsyncTasksHttpExecutor(hosts);
             var executor = new CallbacksHttpExecutor(hosts);
            executor.Execute();
            Thread.Sleep(2000);
        }
    }
}