package java;
import java.util.*;
public class Bank {
    float amount;
    float balance;  
    Bank(float amount, float balance){
        this.balance=balance;
        this.amount=amount;
    }
    void withdraw(float amount){
        balance=balance-amount;
        System.out.println("The balance after withdraw is "+balance);
    }
    void deposit(float amount){
        balance=balance+amount;
        System.out.println("The balance after deposit is "+balance);
    }
    public static void main(String[] args){
        System.out.println("Welcome to the bank");
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter the amount");
        float amount=sc.nextFloat();
        System.out.println("Enter the balance");
        float balance=sc.nextFloat();
        Bank b=new Bank(amount,balance);
        b.withdraw(amount);
        b.deposit(amount);

    }
}
