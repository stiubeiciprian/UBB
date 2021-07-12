package forumWebApp.model;

import forumWebApp.domain.User;
import forumWebApp.exception.FormDatabaseException;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

public class Authenticator extends DBManager {

    public Authenticator(){
        super();
    }

    public User authenticate(String username, String password) {
        User user = null;
        try {
            Connection connection = getConnection();

            String query = "SELECT id, username, password FROM public.\"user\" WHERE username=? and password=?";
            PreparedStatement preparedStatement = connection.prepareStatement(query);
            preparedStatement.setString(1, username);
            preparedStatement.setString(2, password);

            ResultSet resultSet = preparedStatement.executeQuery();

            if(resultSet.next()) {
                int id = resultSet.getInt("id");
                String name = resultSet.getString("username");
                user = new User(id, name, "");
                resultSet.close();
                return user;
            }

            resultSet.close();
        } catch (SQLException e) {
            System.out.println("Authenticator error.");
            e.printStackTrace();
        }  catch (FormDatabaseException e) {
            System.out.println(e.getMessage());
        }
        return user;
    }

    public String register(String username, String password) {
        try {
            Connection connection = getConnection();

            String query = "INSERT INTO public.\"user\"(username, password)  VALUES(?, ?)";
            PreparedStatement preparedStatement = connection.prepareStatement(query);
            preparedStatement.setString(1, username);
            preparedStatement.setString(2, password);

            if(preparedStatement.executeUpdate() != 0) {
                return "success";
            }

        } catch (SQLException e) {
            System.out.println("Registration error.");
        }  catch (FormDatabaseException e) {
            System.out.println(e.getMessage());
        }
        return "error";
    }
}
