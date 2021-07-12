package forumWebApp.exception;

public class FormDatabaseException extends  Exception {
    public FormDatabaseException() {
    }

    public FormDatabaseException(String message) {
        super(message);
    }

    public FormDatabaseException(String message, Throwable cause) {
        super(message, cause);
    }

    public FormDatabaseException(Throwable cause) {
        super(cause);
    }

    public FormDatabaseException(String message, Throwable cause, boolean enableSuppression, boolean writableStackTrace) {
        super(message, cause, enableSuppression, writableStackTrace);
    }
}
