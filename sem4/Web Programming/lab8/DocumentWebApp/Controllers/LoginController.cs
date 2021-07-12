using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;


using DocumentWebApp.Models;
using DocumentWebApp.DataAbstractionLayer;

namespace DocumentWebApp.Controllers
{
    public class LoginController : Controller
    {
        // GET: Login
        public ActionResult Index()
        {
            return View("Login");
        }

        public ActionResult Authenticate()
        {
            User user = new User();
            user.Username = Request.Params["username"];
            user.Password = Request.Params["password"];

            DAL dal = new DAL();
            User checkedUser = dal.Authenticate(user);

            if (checkedUser != null)
            {
                Session["user"] = checkedUser;
                return Redirect(Url.Action("Index", "Main"));
            }
            TempData["message"] = "Username or password are incorrect. Please try again.";
            return Redirect(Url.Action("Index", "Login"));
        }
    }
}