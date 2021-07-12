package forumWebApp.controller;

import forumWebApp.model.Authenticator;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

public class RegisterController extends HttpServlet {
    public RegisterController() {
    }

    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        String username = request.getParameter("username");
        String password = request.getParameter("password");
        RequestDispatcher dispatcher = null;

        Authenticator authenticator = new Authenticator();
        String result = authenticator.register(username, password);

        if(result.equalsIgnoreCase("success")) {
            dispatcher = request.getRequestDispatcher("/login.html");
        } else {
            dispatcher = request.getRequestDispatcher("/register.html#error");
        }
        dispatcher.forward(request, response);
    }
}
