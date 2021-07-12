package forumWebApp.controller;

import com.google.gson.Gson;
import forumWebApp.domain.Comment;
import forumWebApp.domain.User;
import forumWebApp.model.CommnetDBManager;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.List;

public class CommentController extends HttpServlet {
    public CommentController() {
    }

    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        response.setContentType("application/json");
        HttpSession session = request.getSession();
        User user = (User) session.getAttribute("user");

        response.addIntHeader("user", user.getId());
        
        String topicId = request.getParameter("topicId");
        
        if(topicId != null) {
            CommnetDBManager commnetDBManager = new CommnetDBManager();
            List<Comment> comments = commnetDBManager.getCommentByTopicId(topicId);
            Gson gson = new Gson();
            String jsonTopics = gson.toJson(comments);

            PrintWriter out = new PrintWriter(response.getOutputStream());
            out.println(jsonTopics);
            out.flush();
        }

    }

    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        String topicId = request.getParameter("topicId");
        HttpSession session = request.getSession();
        User user = (User) session.getAttribute("user");

        String userId = String.valueOf(user.getId());
        String text = request.getParameter("text");

        CommnetDBManager commnetDBManager = new CommnetDBManager();
        commnetDBManager.addComment(topicId, userId, text);
    }

    @Override
    protected void doDelete(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        String commentId = request.getParameter("id");
        if(commentId != null) {
            CommnetDBManager commnetDBManager = new CommnetDBManager();
            commnetDBManager.deleteComment(commentId);
        }
    }
}
