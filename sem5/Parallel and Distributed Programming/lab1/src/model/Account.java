package model;

import java.util.ArrayList;

public class Account {
    private Integer accountId;
    private ArrayList<Operation> log;
    private Integer amount;

    public Account(Integer accountId, Integer amount) {
        this.accountId = accountId;
        this.log = new ArrayList<Operation>();
        this.amount = amount;
    }

    public Account(Integer accountId, ArrayList<Operation> log, Integer amount) {
        this.accountId = accountId;
        this.log = log;
        this.amount = amount;
    }

    public Integer getAmount() {
        return amount;
    }

    public synchronized void transfer(Integer sum) {
        this.amount = amount + sum;
    }

    public ArrayList<Operation> getLog() {
        return log;
    }

    public synchronized void addToLog(Operation operation) {
        this.log.add(operation);
    }

    public Integer getAccountId() {
        return accountId;
    }

    @Override
    public String toString() {
        return "Account{" +
                "accountId=" + accountId +
                " amount=" + amount +
                ", log=" + log +
                '}';
    }
}
