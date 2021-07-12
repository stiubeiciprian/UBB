package forumWebApp.controller;

import forumWebApp.domain.User;
import forumWebApp.model.Authenticator;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;
import java.io.IOException;


public class LoginController extends HttpServlet {
    public LoginController() {
    }

    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        String username = request.getParameter("username");
        String password = request.getParameter("password");
        RequestDispatcher dispatcher = null;

        Authenticator authenticator = new Authenticator();
        User user = authenticator.authenticate(username, password);

        if(user != null) {
            HttpSession session = request.getSession();
            session.setAttribute("user", user);
            dispatcher = request.getRequestDispatcher("/welcome.jsp");
        } else {
            dispatcher = request.getRequestDispatcher("/error.jsp");
        }

        dispatcher.forward(request, response);
    }
}
