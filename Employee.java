public class Employee{
    int id;
    String name;
    float Salary;
    Employee(){
        id=0;
        name="Harasha";
        Salary=2500000;
    }
    Employee(int id,String name,float Salary){
        this.id=id;
        this.name=name;
        this.Salary=Salary;
    }
    void setsalary(float salary,float bonus){
        this.Salary=salary+bonus;
    }
    void display(){
        System.out.println("The id of the employee is "+id);
        System.out.println("The name of the employee is "+name);
        System.out.println("The salary of the employee is "+Salary);
    }
    public static void main(String[] args){
        Employee e1=new Employee(1,"Sriharshith",250000);
        e1.setsalary(250000,50000);
        e1.display();
        Employee e2=new Employee(2,"Harsha",300000);
        e2.setsalary(300000,60000);
        e2.display();

    }
}
