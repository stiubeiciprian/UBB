package forumWebApp.model;

import forumWebApp.exception.FormDatabaseException;

import java.sql.Connection;
import java.sql.DriverManager;

public class DBManager {

    public Connection getConnection() throws FormDatabaseException {
        try {
            Class.forName("org.postgresql.Driver");
            Connection conn = DriverManager.getConnection("jdbc:postgresql://localhost:5432/forum", "postgres", "cipri");
            return conn;
        } catch (Exception e) {
            throw new FormDatabaseException("Error connecting to the database.");
        }
    }

}
