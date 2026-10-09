class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("\nPerson Details:")
        print("Name:",self.name)
        print("Age:",self.age)
        
class Employee:
    def __init__(self,*args):
        if len(args)==2:
            self.name=args[0]
            self.age=args[1]
            self.__employee_id=None
            self.__salary=0
        elif len(args)==4:
            self.name=args[0]
            self.age=args[1]
            self.__employee_id=args[2]
            self.__salary=args[3]
            
        else:
            
            raise TypeError("Invalid number of arguments")
        
    def get_employee_id(self):
        return self.__employee_id
    def set_employee_id(self,employee_id):
        self.__employee_id=employee_id
    def get_salary(self):
        return self.__salary
    def set_salary(self,salary):
        self.__salary=salary
        
    def display(self):
        print("\nEmployee Details:")
        print("Name:",self.name)
        print("Age:",self.age)
        print("Employee ID:",self.__employee_id)
        print("Salary: $",self.__salary)
        
    def __del__(self):
        print("Employee object destroyed.")
        
    
class Manager(Employee):
    def __init__(self,name,age,employee_id,salary,department):
        super().__init__(name,age,employee_id,salary)
        self.department=department
        
    def display(self):
        print("\nManager Details:")
        print("Name:",self.name)
        print("Age:",self.age)
        print("Employee ID:",self.get_employee_id())
        print("Salary: $",self.get_salary())
        print("Department:",self.department)
        
class Developer(Employee):
    
    def __init__(self,name,age,employee_id,salary,programming_language):
        super().__init__(name,age,employee_id,salary)
        self.programming_language=programming_language
        
    def display(self):
        print("\nDeveloper Details:")
        print("Name:",self.name)
        print("Age:",self.age)
        print("Employee ID:",self.get_employee_id())
        print("Salary: $",self.get_salary())
        print("Programming Language:",self.programming_language)

print("Manager is subclass of Employee:",issubclass(Manager,Employee))
print("Developer is subclass of Employee:",issubclass(Developer,Employee))
        
person=None
employees=[]

while True:
    print("\n--- Python OOP Project: Employee Management System ---")
    print("1. Create a Person")
    print("2. Create an Employee")
    print("3. Create a Manager")
    print("4. Create a Developer")
    print("5. Show details")
    print("6. Update Employee")
    print("7. Remove Employee")
    print("8. Exit")
    
    choice=input("\nEnter your choice: ")
    
    if choice=="1":
        
        name=input("\nEnter Name: ")
        age=int(input("Enter Age: "))
        person=Person(name,age)
        
        print("\nPerson created with name:",name,"and age:",age)
        
    elif choice=="2":
        
        name=input("\nEnter Name: ")
        age=int(input("Enter Age: "))
        employee_id=input("Enter Employee ID: ")
        salary=float(input("Enter Salary: "))
        
        employee=Employee(name,age,employee_id,salary)
        
        employees.append(employee)
        
        print("\nEmployee Details:")
        print("Name:",name)
        print("Age:",age)
        print("Employee ID:",employee_id)
        print("Salary:",salary)
    elif choice=="3":
        
        name=input("\nEnter Name: ")
        age=int(input("Enter Age: "))
        employee_id=input("Enter Employee ID: ")
        salary=float(input("Enter Salary: "))
        department=input("Enter Department: ")
        
        manager=Manager(name,age,employee_id,salary,department)
        
        employees.append(manager)
        
        print("\nManager Details:")
        print("Name:",name)
        print("Age:",age)
        print("Employee ID:",employee_id)
        print("Salary:",salary)
        print("Department:",department)
        
        print(f"Manager created with name: {name}, age: {age}, ID: {employee_id}, salary: ${salary}, and department: {department}.")
        
    elif choice=="4":
        
        name=input("\nEnter Name: ")
        age=int(input("Enter Age: "))
        employee_id=input("Enter Employee ID: ")
        salary=float(input("Enter Salary: "))
        programming_language=input("Enter Programming Language: ")
        
        developer=Developer(name,age,employee_id,salary,programming_language)
        
        employees.append(developer)
        
        print("\nDeveloper Details:")
        print("Name:",name)
        print("Age:",age)
        print("Employee ID:",employee_id)
        print("Salary:",salary)
        print("Programming Language:",programming_language)
        
        print(f"Developer created with name: {name}, age: {age}, ID: {employee_id}, salary: ${salary}, and programming language: {programming_language}.")
        
    elif choice=="5":
        
        print("\nChoose details to show:")
        
        print("1. Person")
        print("2. Employee")
        print("3. Manager")
        print("4. Developer")
        
        detail_choice=input("\nEnter your choice: ")
        
        if detail_choice=="1":
            if person is not None:
                person.display()
            else:
                print("\nNo Person data available.")
                
        elif detail_choice=="2":
            found=False
            for employee in employees:
                if type(employee)==Employee:
                    employee.display()
                    found=True
            if not found:
                print("\nNo Employee data available.")
                
        elif detail_choice=="3":
            found=False
            for employee in employees:
                if isinstance(employee,Manager):
                    employee.display()
                    found=True
            if not found:
                print("\nNo Manager data available.")
                
        elif detail_choice=="4":
            found=False
            for employee in employees:
                if isinstance(employee,Developer):
                    employee.display()
                    found=True
            if not found:
                print("\nNo Developer data available.")
        else:
            print("\nInvalid choice.")
            
    elif choice=="6":
        
        employee_id=input("\nEnter Employee ID to update: ")
        found=False
        for employee in employees:
            if employee.get_employee_id()==employee_id:
                print("\n1. Update Name")
                print("2. Update Age")
                print("3. Update Salary")
                print("4. Update Employee ID")
                update_choice=input("\nEnter your choice: ")
                if update_choice=="1":
                    employee.name=input("Enter New Name: ")
                elif update_choice=="2":
                    employee.age=int(input("Enter New Age: "))
                elif update_choice=="3":
                    employee.set_salary(float(input("Enter New Salary: ")))
                elif update_choice=="4":
                    employee.set_employee_id(input("Enter New Employee ID: "))
                else:
                    print("\nInvalid choice.")
                    break
                print("\nEmployee updated successfully.")
                found=True
                break
        if not found:
            print("\nEmployee not found.")
            
    elif choice=="7":
        
        employee_id=input("\nEnter Employee ID to remove: ")
        found=False
        for employee in employees:
            if employee.get_employee_id()==employee_id:
                employees.remove(employee)
                print("\nEmployee removed successfully.")
                found=True
                break
        if not found:
            print("\nEmployee not found.")
            
    elif choice=="8":
        
        print("\nExiting the system.")
        print("All resources have been freed.")
        print("\nGoodbye!")
        
        break
    else:
        print("\nInvalid choice!")
        print("Please enter a valid choice.")
