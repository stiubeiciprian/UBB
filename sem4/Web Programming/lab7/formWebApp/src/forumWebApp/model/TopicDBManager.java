package forumWebApp.model;

import forumWebApp.domain.Topic;
import forumWebApp.exception.FormDatabaseException;

import java.sql.*;
import java.util.ArrayList;
import java.util.List;

public class TopicDBManager extends DBManager {

    public void addTopic(String title, String text, String userId) {
        try {
            Connection connection = getConnection();

            String query = "INSERT INTO public.topic(title, text, \"userId\") VALUES (?,?,?)";
            PreparedStatement statement = connection.prepareStatement(query);
            statement.setString(1, title);
            statement.setString(2, text);
            statement.setInt(3, Integer.parseInt(userId));
            statement.executeUpdate();
        } catch (SQLException e) {
            System.out.println("Failed to add topic.");
        }  catch (FormDatabaseException e) {
            System.out.println(e.getMessage());
        }
    }

    public List<Topic> getAllTopics() {
        ArrayList<Topic> topics = new ArrayList<>();

        try {
            Connection connection = getConnection();

            String query = "SELECT * FROM public.\"topic\"";
            Statement statement = connection.createStatement();
            ResultSet resultSet = statement.executeQuery(query);

            while (resultSet.next()) {
                String title = resultSet.getString("title");
                String text = resultSet.getString("text");
                String author = "Anonymous";
                Integer id = resultSet.getInt("id");

                topics.add(new Topic(title, text, author, id));
            }
            resultSet.close();
            return topics;

        } catch (SQLException e) {
            System.out.println("Failed to fetch topics.");
        }  catch (FormDatabaseException e) {
            System.out.println(e.getMessage());
        }
        return topics;
    }

    public Topic getTopicById(String topicId) {
        Topic topic = new Topic();
        try {
            Connection connection = getConnection();

            String query = "SELECT * FROM public.\"topic\" WHERE id=?";
            PreparedStatement statement = connection.prepareStatement(query);
            statement.setInt(1, Integer.parseInt(topicId));

            ResultSet resultSet = statement.executeQuery();

            if (resultSet.next()) {
                topic.setTitle(resultSet.getString("title"));
                topic.setText(resultSet.getString("text"));
                topic.setAuthor("Anonymous");
                topic.setId(resultSet.getInt("id"));
            }
            resultSet.close();
            return topic;

        } catch (SQLException e) {
            System.out.println("Failed to fetch topic by id.");
        }  catch (FormDatabaseException e) {
            System.out.println(e.getMessage());
        }
        return topic;
    }
}
