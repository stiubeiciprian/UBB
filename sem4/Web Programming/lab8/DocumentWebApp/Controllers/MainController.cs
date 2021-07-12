using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;

using DocumentWebApp.Models;
using DocumentWebApp.DataAbstractionLayer;

namespace DocumentWebApp.Controllers
{
    public class MainController : Controller
    {
        // GET: Main
        public ActionResult Index()
        {
            if (Session["user"] == null)
            {
                return Redirect(Url.Action("Index", "Login"));
            }

                return View("Documents");
        }

        public ActionResult AddDocument()
        {
            if (Session["user"] == null)
            {
                return Redirect(Url.Action("Index", "Login"));
            }

            return View("AddDocument");
        }


        public ActionResult UpdateDocument()
        {
            if (Session["user"] == null)
            {
                return Redirect(Url.Action("Index", "Login"));
            }

            if (Request.Params["id"] == null)
            {
                return View("Documents");
            }

            int id = int.Parse(Request.Params["id"]);

            DAL dal = new DAL();
            Document document = dal.GetDocumentById(id);

            ViewData["document"] = document;

            return View("UpdateDocument");
        }




        public JsonResult GetDocuments()
        {

            DAL dal = new DAL();
            List<Document> documents = dal.GetAllDocuments();
            
            return Json(documents, JsonRequestBehavior.AllowGet);
        }

        public ActionResult Add()
        {
            if (Session["user"] == null)
            {
                return Redirect(Url.Action("Index", "Login"));
            }


            string[] paramArray = {"title", "author", "pages", "type", "format" };
            if (validateRequestParams(paramArray))
            {
                return Redirect(Url.Action("AddDocument", "Main"));
            }

            Document doc = new Document();
            doc.Title = Request.Params["title"];
            doc.Author = Request.Params["author"];
            doc.NumberOfPages = int.Parse(Request.Params["pages"]);
            doc.Type = Request.Params["type"];
            doc.Format = Request.Params["format"];

            DAL dal = new DAL();
            dal.AddDocument(doc);

            return Redirect(Url.Action("Index", "Main"));

        }

        public ActionResult Update()
        {
            if (Session["user"] == null)
            {
                return Redirect(Url.Action("Index", "Login"));
            }

            DAL dal = new DAL();

            string[] paramArray = {"id", "title","author","pages","type","format"};
            if (validateRequestParams(paramArray))
            {

                Document document = dal.GetDocumentById(int.Parse(Request.Params["id"]));
                ViewData["document"] = document;
                return Redirect(Url.Action("UpdateDocument", "Main"));
            }

            Document doc = new Document();
            doc.Id = int.Parse(Request.Params["id"]);
            doc.Title = Request.Params["title"];
            doc.Author = Request.Params["author"];
            doc.NumberOfPages = int.Parse(Request.Params["pages"]);
            doc.Type = Request.Params["type"];
            doc.Format = Request.Params["format"];

            dal.UpdateDocument(doc);
            ViewData["document"] = doc;

            return Redirect(Url.Action("Index", "Main"));

        }

        private Boolean validateRequestParams(String[] paramArray)
        {

            foreach(String param in paramArray)
            {
                if(Request.Params[param] == "null")
                {
                    return false;
                }
            }

            return true;
        }


        public void Delete()
        {
            int id = int.Parse(Request.Params["id"]);

            DAL dal = new DAL();
            dal.DeleteDocument(id);
        }

    }
}