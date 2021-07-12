package model;

public class Operation {
    private Integer serialNumber;
    private Integer sourceAccount;
    private Integer destinationAccount;
    private Integer amount;

    public Operation(Integer serialNumber, Integer sourceAccount, Integer destinationAccount, Integer amount) {
        this.serialNumber = serialNumber;
        this.sourceAccount = sourceAccount;
        this.destinationAccount = destinationAccount;
        this.amount = amount;
    }

    public Integer getSerialNumber() {
        return serialNumber;
    }

    public void setSerialNumber(Integer serialNumber) {
        this.serialNumber = serialNumber;
    }

    public Integer getSourceAccount() {
        return sourceAccount;
    }

    public void setSourceAccount(Integer sourceAccount) {
        this.sourceAccount = sourceAccount;
    }

    public Integer getDestinationAccount() {
        return destinationAccount;
    }

    public void setDestinationAccount(Integer destinationAccount) {
        this.destinationAccount = destinationAccount;
    }

    public Integer getAmount() {
        return amount;
    }

    public void setAmount(Integer amount) {
        this.amount = amount;
    }

    @Override
    public String toString() {
        return "Operation{" +
                "serialNumber=" + serialNumber +
                ", source=" + sourceAccount +
                ", destination=" + destinationAccount +
                ", amount=" + amount +
                '}';
    }
}
