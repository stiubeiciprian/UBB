package forumWebApp.model;

import forumWebApp.domain.Comment;
import forumWebApp.exception.FormDatabaseException;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;

public class CommnetDBManager extends DBManager {

    public void addComment(String topicId, String userId, String text) {
        try {
            Connection connection = getConnection();

            String query = "INSERT INTO public.comment(text, \"authorId\", \"topicId\") VALUES (?,?,?)";
            PreparedStatement statement = connection.prepareStatement(query);
            statement.setString(1, text);
            statement.setInt(2, Integer.parseInt(userId));
            statement.setInt(3, Integer.parseInt(topicId));
            statement.executeUpdate();
        } catch (SQLException e) {
            System.out.println("Failed to add comment.");
        }  catch (FormDatabaseException e) {
            System.out.println(e.getMessage());
        }
    }

    public void deleteComment(String commentId) {
        try {
            Connection connection = getConnection();

            String query = "DELETE FROM public.comment WHERE id=?";
            PreparedStatement statement = connection.prepareStatement(query);
            statement.setInt(1, Integer.parseInt(commentId));
            statement.executeUpdate();
        } catch (SQLException e) {
            System.out.println("Failed to delete comment.");
        }  catch (FormDatabaseException e) {
            System.out.println(e.getMessage());
        }
    }


    public List<Comment> getCommentByTopicId(String topicId) {
        ArrayList<Comment> comments = new ArrayList<>();

        try {
            Connection connection = getConnection();

            String query = "SELECT * FROM public.\"comment\" WHERE \"topicId\"=?";
            PreparedStatement statement = connection.prepareStatement(query);
            statement.setInt(1, Integer.parseInt(topicId));
            ResultSet resultSet = statement.executeQuery();

            while (resultSet.next()) {
                int id = resultSet.getInt("id");
                int userId = resultSet.getInt("authorId");
                String text = resultSet.getString("text");
                String author = getCommentAuthor(userId);

                comments.add(new Comment(id, userId, author, text));
            }
            resultSet.close();
            return comments;

        } catch (SQLException e) {
            System.out.println("Failed to fetch comments.");
        }  catch (FormDatabaseException e) {
            System.out.println(e.getMessage());
        }
        return comments;
    }

    private String getCommentAuthor(int userId) {
        String author ="Anonymous";
        try {
            Connection connection = getConnection();

            String query = "SELECT * FROM public.\"user\" WHERE id=?";
            PreparedStatement statement = connection.prepareStatement(query);
            statement.setInt(1, userId);

            ResultSet resultSet = statement.executeQuery();

            if (resultSet.next()) {
                author = resultSet.getString("username");
            }
            resultSet.close();
            return author;

        } catch (SQLException e) {
            System.out.println("Failed to get author name.");
        }  catch (FormDatabaseException e) {
            System.out.println(e.getMessage());
        }
        return author;
    }



}
