<div align="center">
<br>

🧩✨ OOP WRAPPER ✨🧩

⚡ PYTHON • OBJECT-ORIENTED PROGRAMMING ⚡

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

💼 Employee Management System

Turning Python OOP Concepts into Practical Code.
<br>
<br>
🔹 CLASSES & OBJECTS　🔹 INHERITANCE　🔹 ENCAPSULATION　🔹 POLYMORPHISM
<br>
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
</div>

✨ About the Project

OOP Wrapper is a Python console application that manages basic person and employee information. It uses classes and objects to represent a Person, an Employee, a Manager, and a Developer.

The project is designed to demonstrate how OOP concepts can be used in a practical, menu-driven program.

🚀 Features

|Icon|Feature         |Description                                            |
|:--:|----------------|-------------------------------------------------------|
|👤   |Create Person   |Store a person’s name and age                          |
|🧑‍💼   |Create Employee |Add employee details, ID, and salary                   |
|🧑‍💻   |Create Manager  |Add a manager with a department                        |
|💻   |Create Developer|Add a developer with a programming language            |
|🔎   |View Details    |Display person, employee, manager, or developer details|
|✏️   |Update Employee |Update name, age, salary, or employee ID               |
|🗑️   |Remove Employee |Remove an employee using their ID                      |
|🚪   |Exit            |Exit the application                                   |


🧠 OOP Concepts Used

• Classes and Objects: Person, Employee, Manager, and Developer model the entities in the application.
• Inheritance: Manager and Developer inherit from Employee.
• Encapsulation: Employee ID and salary are stored as private attributes and accessed through getter/setter methods.
• Polymorphism / Method Overriding: Manager and Developer provide their own display() methods.
• Constructor Overloading Pattern: Employee accepts different argument counts using *args.
• super(): Child classes call the parent Employee constructor.
• Built-in Type Checks: issubclass() and isinstance() are used to check class relationships and object types.


<h2 align="center">🔄 OOP Wrapper - Application Flow</h2>
<div align="center">
<pre>
          ┌───────────────┐
          │     START     │
          └───────┬───────┘
                  ↓
          ┌───────────────┐
          │  Main Menu    │
          └───────┬───────┘
                  ↓
          ┌────────────────────┐
          │   Select Option    │
          └─────────┬──────────┘
                    ↓
   ┌─────────────────────────────────┐
   │ 1. Create Person                │
   │ 2. Create Employee              │
   │ 3. Create Manager               │
   │ 4. Create Developer             │
   │ 5. Show Details                 │
   │ 6. Update Employee              │
   │ 7. Remove Employee              │
   └────────────────┬────────────────┘
                    ↓
          ┌───────────────────┐
          │  Process Request  │
          └─────────┬─────────┘
                    ↓
          ┌───────────────────┐
          │  Return to Menu   │
          └─────────┬─────────┘
                    ↓
          ┌───────────────────┐
          │  8. Exit Program  │
          └───────────────────┘
</pre>
</div>


🖥️ Sample Output

The following is an example of the application’s console output using sample inputs:

```text
Manager is subclass of Employee: True
Developer is subclass of Employee: True

--- Python OOP Project: Employee Management System ---
1. Create a Person
2. Create an Employee
3. Create a Manager
4. Create a Developer
5. Show details
6. Update Employee
7. Remove Employee
8. Exit

Enter your choice: 2

Enter Name: Kavy
Enter Age: 21
Enter Employee ID: D101
Enter Salary: 45000

Employee Details:
Name: Kavy
Age: 21
Employee ID: D101
Salary: 45000.0
```

✏️ Example: Updating an Employee

```text
Enter Employee ID to update: D101

1. Update Name
2. Update Age
3. Update Salary
4. Update Employee ID

Enter your choice: 3
Enter New Salary: 56000

Employee updated successfully.
```

🗑️ Example: Removing an Employee

```text
Enter Employee ID to remove: D102

Employee removed successfully.
