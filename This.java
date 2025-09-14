import java.util.*;
class BankAccount{
    String accountHolder;
    int accountNumber;
    double balance;
    BankAccount(){
        this("Unknown",0,0.0);
        System.out.println("Default account created");
    }
    BankAccount(String accountHolder,int accountNumber,double balance){
        this.accountHolder=accountHolder;
        this.accountNumber=accountNumber;
        this.balance=balance;
    }
    BankAccount deposit(double amount){
        this.balance=balance+amount;
        return this;
    }
    BankAccount withdraw(double amount){
        balance=balance-amount;
        return this;
    }
    void displayAccount() {
        System.out.println("AccountHolder: " + this.accountHolder + 
                           ", AccountNumber: " + this.accountNumber +
                           ", Balance: $" + this.balance);
    }
    void transfer(BankAccount target,double amount){
        this.balance=this.balance-amount;
        target.balance+=amount;
        System.out.println("Transfered "+amount+" to" +target.accountHolder);
    }
    class TransactionLogger{
        void logTransaction(String type,double amount){
            System.out.println("Transaction: " + type + ", Amount: $" + amount + 
                               ", AccountHolder: " + BankAccount.this.accountHolder);

        }
    }
    public class This{
        public static void main(String[] args) {
            BankAccount a1=new BankAccount("Alice", 101, 500.0);
            BankAccount a2=new BankAccount("Bob", 102, 300.0);
            a1.deposit(200).deposit(500).withdraw(345).displayAccount();
            a1.transfer(a2,100);
            BankAccount.TransactionLogger logger=a1.new TransactionLogger();
            logger.logTransaction("Deosit", 20000);
             BankAccount acc3 = new BankAccount();
             acc3.displayAccount();
        }
    }

}
