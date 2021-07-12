package ubb.client;

import org.springframework.context.annotation.AnnotationConfigApplicationContext;
import ubb.client.ui.Console;

public class ClientApp {


    public static void main(String[] args) {
        AnnotationConfigApplicationContext context =
                new AnnotationConfigApplicationContext(
                        "ubb.client.config"
                );

        Console console = context.getBean(Console.class);
        console.runConsole();
    }

}