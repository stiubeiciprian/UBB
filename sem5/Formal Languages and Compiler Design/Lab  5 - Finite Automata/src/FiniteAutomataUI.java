import java.io.IOException;
import java.util.Scanner;

public class FiniteAutomataUI {
    private static final String menu = "\nMenu\n1.States\n2.Alphabet\n3.Transitions\n4.Final states\n5.Initial state\n6.Check sequence\n0.Exit\n";

    public static String readSequence() {
        System.out.print("Enter sequence: ");
        Scanner scanner = new Scanner(System.in);
        return scanner.nextLine();
    }

    public static void main(String[] args) {
        FiniteAutomata fa = new FiniteAutomata();

        try {
            fa.readFromFile("E:\\UBB\\sem5\\Formal Languages and Compiler Design\\Labs - git\\Lab  5 - Finite Automata\\src\\FA.in");
        } catch (IOException e) {
            e.printStackTrace();
        }

        Scanner scanner = new Scanner(System.in);
        while (true) {
            System.out.println(menu);

            System.out.print(">>");
            int command = scanner.nextInt();

            switch (command) {
                case 1:
                    System.out.println("States:\n" + fa.getStates());
                    break;
                case 2:
                    System.out.println("Alphabet:\n" + fa.getAlphabet());
                    break;
                case 3:
                    System.out.println("Transitions:");
                    fa.getTransitions().forEach(System.out::println);
                    break;
                case 4:
                    System.out.println("Final states:\n" + fa.getFinalStates());
                    break;
                case 5:
                    System.out.println("Starting state:\n" + fa.getStartingState());
                    break;
                case 6:
                    String sequence = readSequence();
                    System.out.println(fa.checkSequence(sequence));
                    break;
                case 0:
                    return;
            }
        }
    }
}