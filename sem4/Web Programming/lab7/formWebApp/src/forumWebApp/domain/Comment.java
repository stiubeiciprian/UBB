package forumWebApp.domain;

public class Comment {
    private int id;
    private int userId;
    private String author;
    private String text;

    public Comment() {
    }

    public Comment(int id, int userId, String author, String text) {
        this.id = id;
        this.userId = userId;
        this.author = author;
        this.text = text;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public int getUserId() {
        return userId;
    }

    public void setUserId(int userId) {
        this.userId = userId;
    }

    public String getAuthor() {
        return author;
    }

    public void setAuthor(String author) {
        this.author = author;
    }

    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }
}


