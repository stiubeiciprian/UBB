import model.Account;
import model.Operation;

import java.util.ArrayList;
import java.util.Random;

public class Bank {
    private static final int NUMBER_OF_ACCOUNTS = 1000;
    private static final int BASE_ACCOUNT_AMOUNT = 5000;

    private static final int NUMBER_OF_THREADS = 2;
    private static final int NUMBER_OF_OPERATION_PER_THREAD = 10000;

    private static int operationSerialNumber = 0;
    private static ArrayList<Account> accounts;
    private static Random rand;

    public static void main(String[] args) {
        rand = new Random();
        accounts = createAccounts();

        ArrayList<Thread> threads = new ArrayList<>();

        for (int i = 0; i < NUMBER_OF_THREADS ; i++) {
            threads.add(new Thread(Bank::runTransfers));
        }
        
        long tic = System.nanoTime();
        
        threads.forEach(Thread::start);
        threads.forEach(t -> {
            try {
                t.join();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        });

        long toc = System.nanoTime();

        long timeOfExecution = toc - tic;
        System.out.println("Running on " + NUMBER_OF_THREADS + " threads with " + NUMBER_OF_OPERATION_PER_THREAD + " operations per thread and " + NUMBER_OF_ACCOUNTS  + " accounts:" );
        System.out.println("Duration: " + timeOfExecution / 1000000 + "ms");
        System.out.println("Consistency test passed: " + checkConsistency());

        //accounts.forEach(System.out::println);
    }

    private static void runTransfers() {
        int operationNumber = NUMBER_OF_OPERATION_PER_THREAD;
        while(operationNumber != 0) {
            transfer();
            if(operationNumber % 1000 == 0) {
                System.out.println("Consistent: " + checkConsistency());
            }
            operationNumber--;
        }
    }

    private static void transfer() {
        int sender = rand.nextInt(NUMBER_OF_ACCOUNTS);
        int receiver = rand.nextInt(NUMBER_OF_ACCOUNTS);
        Integer amount = rand.nextInt(300);

        Operation operation = new Operation(getOperationSerialNumber(), sender, receiver, amount);

        Account senderAccount = accounts.get(sender);
        Account receiverAccount = accounts.get(receiver);
        transferMoney(senderAccount, receiverAccount, operation);
    }

    private static void transferMoney(Account sender, Account receiver,Operation operation) {
        sender.transfer(-operation.getAmount());
        sender.addToLog(operation);

        receiver.transfer(operation.getAmount());
        receiver.addToLog(operation);
    }

    private static ArrayList<Account> createAccounts() {
        ArrayList<Account> accounts = new ArrayList<>();

        for (int i = 0; i < NUMBER_OF_ACCOUNTS; i++) {
            accounts.add(new Account(i, BASE_ACCOUNT_AMOUNT));
        }

        return accounts;
    }

    private static Boolean checkConsistency() {
        return accounts.stream().mapToInt(Account::getAmount).sum() == NUMBER_OF_ACCOUNTS * BASE_ACCOUNT_AMOUNT;

    }

    private synchronized static Integer getOperationSerialNumber() {
        operationSerialNumber+=1;
        return operationSerialNumber;
    }
}
