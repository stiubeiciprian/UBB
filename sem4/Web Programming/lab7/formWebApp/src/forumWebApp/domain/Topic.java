package forumWebApp.domain;

public class Topic {
    private String title;
    private String text;
    private String author;
    private Integer id;

    public Topic() {
    }

    public Topic(String title, String text, String author, Integer id) {
        this.title = title;
        this.text = text;
        this.author = author;
        this.id = id;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }

    public String getAuthor() {
        return author;
    }

    public void setAuthor(String author) {
        this.author = author;
    }

    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }
}
