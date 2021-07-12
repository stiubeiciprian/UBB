using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;


using DocumentWebApp.Models;
using MySql.Data.MySqlClient;

namespace DocumentWebApp.DataAbstractionLayer
{
    public class DAL
    {

        private static string connectionString = "datasource=127.0.0.1;port=3306;username=root;pwd=;database=documents_db;";

        public List<Document> GetAllDocuments()
        {
            List<Document> documents = new List<Document>();

            try
            {
                MySql.Data.MySqlClient.MySqlConnection conn = new MySql.Data.MySqlClient.MySqlConnection();
                conn.ConnectionString = connectionString;
                conn.Open();

                MySqlCommand cmd = new MySqlCommand();
                cmd.Connection = conn;
                cmd.CommandText = "SELECT * FROM document";
                MySqlDataReader dataReader = cmd.ExecuteReader();

                while (dataReader.Read())
                {
                    Document doc = new Document();
                    doc.Id = dataReader.GetInt32("id");
                    doc.Title = dataReader.GetString("title");
                    doc.Author = dataReader.GetString("author");
                    doc.Format = dataReader.GetString("format");
                    doc.NumberOfPages = dataReader.GetInt32("numberOfPages");
                    doc.Type = dataReader.GetString("type");
                    documents.Add(doc);
                }
                dataReader.Close();
            }
            catch (MySql.Data.MySqlClient.MySqlException ex)
            {
                Console.Write(ex.Message);
            }
            return documents;
        }

        internal Document GetDocumentById(int id)
        {
            Document doc = new Document();

            try
            {
                MySql.Data.MySqlClient.MySqlConnection conn = new MySql.Data.MySqlClient.MySqlConnection();
                conn.ConnectionString = connectionString;
                conn.Open();

                MySqlCommand cmd = new MySqlCommand();
                cmd.Connection = conn;
                cmd.CommandText = "SELECT * FROM document WHERE id=" + id;
                MySqlDataReader dataReader = cmd.ExecuteReader();

                if (dataReader.Read())
                {
                    doc.Id = dataReader.GetInt32("id");
                    doc.Title = dataReader.GetString("title");
                    doc.Author = dataReader.GetString("author");
                    doc.Format = dataReader.GetString("format");
                    doc.NumberOfPages = dataReader.GetInt32("numberOfPages");
                    doc.Type = dataReader.GetString("type");
                }
                dataReader.Close();
            }
            catch (MySql.Data.MySqlClient.MySqlException ex)
            {
                Console.Write(ex.Message);
            }
            return doc;
        }

        public void AddDocument(Document document)
        {
            try
            {
                MySql.Data.MySqlClient.MySqlConnection conn = new MySql.Data.MySqlClient.MySqlConnection();
                conn.ConnectionString = connectionString;
                conn.Open();

                MySqlCommand cmd = new MySqlCommand();
                cmd.Connection = conn;
                cmd.CommandText = "INSERT INTO document(title, author, numberOfPages, format, type) " +
                    "VALUES('"+ document.Title +"', '"+ document.Author + "', '"+ document.NumberOfPages +"', '" + document.Format +"', '"+document.Type +"')";
                cmd.ExecuteNonQuery();
            }
            catch (MySql.Data.MySqlClient.MySqlException ex)
            {
                Console.Write(ex.Message);
            }
        }

        public void UpdateDocument(Document document)
        {
            try
            {
                MySql.Data.MySqlClient.MySqlConnection conn = new MySql.Data.MySqlClient.MySqlConnection();
                conn.ConnectionString = connectionString;
                conn.Open();

                MySqlCommand cmd = new MySqlCommand();
                cmd.Connection = conn;
                cmd.CommandText = "UPDATE document SET title='"+document.Title+"', author='"+document.Author+"', numberOfPages="+document.NumberOfPages+", format='"+document.Format+"', type='"+document.Type+"' WHERE id=" + document.Id;
                cmd.ExecuteNonQuery();
            }
            catch (MySql.Data.MySqlClient.MySqlException ex)
            {
                Console.Write(ex.Message);
            }
        }
        public void DeleteDocument(int id)
        {
            try
            {
                MySql.Data.MySqlClient.MySqlConnection conn = new MySql.Data.MySqlClient.MySqlConnection();
                conn.ConnectionString = connectionString;
                conn.Open();

                MySqlCommand cmd = new MySqlCommand();
                cmd.Connection = conn;
                cmd.CommandText = "DELETE FROM document WHERE id=" + id;
                cmd.ExecuteNonQuery();
            }
            catch (MySql.Data.MySqlClient.MySqlException ex)
            {
                Console.Write(ex.Message);
              
            }
        }

        public User Authenticate(User user)
        {

            try
            {
                MySql.Data.MySqlClient.MySqlConnection conn = new MySql.Data.MySqlClient.MySqlConnection();
                conn.ConnectionString = connectionString;
                conn.Open();

               
                MySqlCommand cmd = new MySqlCommand();
                cmd.Connection = conn;
                cmd.CommandText = "SELECT * FROM user WHERE username='" + user.Username + "' AND password='" + user.Password + "'";
                MySqlDataReader dataReader = cmd.ExecuteReader();


                if (dataReader.Read())
                {
                    User checkedUser = new User();
                    checkedUser.Id = dataReader.GetInt32("id");
                    checkedUser.Username = dataReader.GetString("username");
 
                    return checkedUser;
                }
            }
            catch (MySql.Data.MySqlClient.MySqlException ex)
            {
                Console.Write(ex.Message);
            }

            return null;
        }
    }
}