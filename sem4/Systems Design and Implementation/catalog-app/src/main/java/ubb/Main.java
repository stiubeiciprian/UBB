package ubb;

import org.springframework.context.annotation.AnnotationConfigApplicationContext;
import ubb.ui.Console;

public class Main {
    public static void main(String[] args) {
        AnnotationConfigApplicationContext context =
                new AnnotationConfigApplicationContext(
                        "ubb"
                );

        Console console = context.getBean(Console.class);
        console.runConsole();
    }


}
