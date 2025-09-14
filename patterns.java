import java.util.*;
public class patterns {
    public static void main(String[] args){
        int r,c;
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter the number of rows:");
        r=sc.nextInt();
        System.out.println("Enter the number of columns:");
        c=sc.nextInt();
        int arr[][]=new int[r][c];
        int i=0,j=0;
         for(i=0;i<r;i++){
            for(j=0;j<c;j++){
               if(i==0 ||i==r-1 ||j==0||j==c-1) {
                System.out.print("* ");
               }
               else{

                System.out.print("  ");
               }
            }
            System.out.println();
        }
    }
}
