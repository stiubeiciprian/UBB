package forumWebApp.controller;


import com.google.gson.Gson;
import forumWebApp.domain.Topic;
import forumWebApp.domain.User;
import forumWebApp.model.TopicDBManager;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.List;

public class TopicController extends HttpServlet {
    public TopicController() {
    }


    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        HttpSession session = request.getSession();
        User user = (User) session.getAttribute("user");
        String userId = String.valueOf(user.getId());

        String title = request.getParameter("title");
        String text = request.getParameter("text");

        TopicDBManager topicDBManager = new TopicDBManager();
        topicDBManager.addTopic(title, text, userId);
    }

    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        response.setContentType("application/json");
        String topicId = request.getParameter("id");


        if(topicId != null) {
            getTopic(request, response, topicId);
            return;
        }

        getAllTopics(response);
    }

    protected void getAllTopics(HttpServletResponse response) throws IOException {
        TopicDBManager topicDBManager = new TopicDBManager();
        List<Topic> topics = topicDBManager.getAllTopics();
        Gson gson = new Gson();
        String jsonTopics = gson.toJson(topics);

        PrintWriter out = new PrintWriter(response.getOutputStream());
        out.println(jsonTopics);
        out.flush();
    }

    protected void getTopic(HttpServletRequest request, HttpServletResponse response, String topicId) throws IOException, ServletException {
        TopicDBManager topicDBManager = new TopicDBManager();
        Topic topic = topicDBManager.getTopicById(topicId);
        request.setAttribute("topic", topic);
        RequestDispatcher dispatcher = request.getRequestDispatcher("/topic.jsp");
        dispatcher.forward(request, response);
    }
}
