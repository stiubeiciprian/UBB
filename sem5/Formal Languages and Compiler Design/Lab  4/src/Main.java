import java.io.IOException;


public class Main {
    public static void main(String[] args) {

        Scanner scanner = new Scanner("E:\\UBB\\sem5\\Formal Languages and Compiler Design\\Labs - git\\Lab  4\\src\\programfiles\\p1.in");

        try {
            scanner.scan();
            scanner.saveProgramInternalFormToFile("PIF.out");
            scanner.saveSymbolTableToFile("ST.out");
        } catch (IOException e) {
            e.printStackTrace();
        }

    }
}
