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
<h2 align="center">🌈 OOP Wrapper – Complete Application Flow</h2>
<h3 align="center">Employee Management System</h3>

<div align="center">

<table>
<tr>
<td align="center" bgcolor="#D9EAF7">

<b>🚀 START</b>

</td>
</tr>
<tr><td align="center">⬇️</td></tr>
<tr>
<td align="center" bgcolor="#E8DAEF">

<b>🔍 Check Inheritance</b><br>
Manager → Employee: True<br>
Developer → Employee: True

</td>
</tr>
<tr><td align="center">⬇️</td></tr>
<tr>
<td align="center" bgcolor="#D5F5E3">

<b>🏠 MAIN MENU</b><br><br>
1. Create a Person<br>
2. Create an Employee<br>
3. Create a Manager<br>
4. Create a Developer<br>
5. Show Details<br>
6. Update Employee<br>
7. Remove Employee<br>
8. Exit

</td>
</tr>
<tr><td align="center">⬇️</td></tr>
<tr>
<td align="center" bgcolor="#FCF3CF">

<b>👤 1. CREATE PERSON</b><br><br>
Name: Bhavik<br>
Age: 26<br>
✅ Person Created Successfully

</td>
</tr>
<tr><td align="center">⬇️</td></tr>
<tr>
<td align="center" bgcolor="#D6EAF8">

<b>👨‍💼 2. CREATE EMPLOYEE</b><br><br>
Name: Kavy<br>
Age: 21<br>
Employee ID: D101<br>
Salary: 45000.0<br><br>
Name: Nipa<br>
Age: 24<br>
Employee ID: D102<br>
Salary: 35000.0

</td>
</tr>
<tr><td align="center">⬇️</td></tr>
<tr>
<td align="center" bgcolor="#FADBD8">

<b>👔 3. CREATE MANAGER</b><br><br>
Name: Yash<br>
Age: 26<br>
Employee ID: M123<br>
Salary: 80000.0<br>
Department: sales<br><br>
✅ Manager Created Successfully

</td>
</tr>
<tr><td align="center">⬇️</td></tr>
<tr>
<td align="center" bgcolor="#E8DAEF">

<b>💻 4. CREATE DEVELOPER</b><br><br>
Name: khushi<br>
Age: 20<br>
Employee ID: A111<br>
Salary: 60000.0<br>
Programming Language: python<br><br>
✅ Developer Created Successfully

</td>
</tr>
<tr><td align="center">⬇️</td></tr>
<tr>
<td align="center" bgcolor="#D5F5E3">

<b>📋 5. SHOW DETAILS</b><br><br>
1. Person → Bhavik<br>
2. Employee → Kavy / Nipa<br>
3. Manager → Yash<br>
4. Developer → khushi<br><br>
📌 Display Selected Details

</td>
</tr>
<tr><td align="center">⬇️</td></tr>
<tr>
<td align="center" bgcolor="#FCF3CF">

<b>✏️ 6. UPDATE EMPLOYEE</b><br><br>
Employee ID: D101<br>
Update Field: Salary<br>
New Salary: 56000<br><br>
✅ Employee Updated Successfully

</td>
</tr>
<tr><td align="center">⬇️</td></tr>
<tr>
<td align="center" bgcolor="#F5CBA7">

<b>🗑️ 7. REMOVE EMPLOYEE</b><br><br>
Employee ID: D102<br><br>
✅ Employee Removed Successfully

</td>
</tr>
<tr><td align="center">⬇️</td></tr>
<tr>
<td align="center" bgcolor="#D5F5E3">

<b>🔁 RETURN TO MAIN MENU</b><br><br>
After each operation, the menu appears again.

</td>
</tr>
<tr><td align="center">⬇️</td></tr>
<tr>
<td align="center" bgcolor="#D6EAF8">

<b>🚪 8. EXIT PROGRAM</b><br><br>
All resources have been closed.<br>
<b>Goodbye!</b>

</td>
</tr>
<tr><td align="center">⬇️</td></tr>
<tr>
<td align="center" bgcolor="#A9DFBF">




<b>🏁 END</b>

</td>
</tr>
</table>

</div>

<h2 align="center">🏗️ OOP Wrapper — Project Architecture</h2>

```mermaid
flowchart TD
    A(["🚀 OOP Wrapper Project"]) --> B["Python OOP Concepts"]

    B --> C["Classes and Objects"]
    B --> D["Inheritance"]
    B --> E["Encapsulation"]
    B --> F["Polymorphism"]
    B --> G["Constructor Overloading Pattern"]

    C --> H["Person Class"]
    H --> I["Employee Class"]

    I --> J["Manager Class"]
    I --> K["Developer Class"]

    D --> L["Manager inherits Employee"]
    D --> M["Developer inherits Employee"]

    E --> N["Private Employee ID"]
    E --> O["Private Salary"]
    N --> P["Getter and Setter Methods"]
    O --> P

    F --> Q["Method Overriding"]
    Q --> R["display() Method"]

    G --> S["Employee Constructor"]
    S --> T["Variable Arguments: *args"]

    H --> U["Name and Age"]
    I --> V["Employee ID and Salary"]
    J --> W["Department"]
    K --> X["Programming Language"]

    U --> Y["Employee Management System"]
    V --> Y
    W --> Y
    X --> Y

    Y --> Z["Create and Display Objects"]
    Y --> AA["Update Employee"]
    Y --> AB["Remove Employee"]
    Y --> AC["Show Details"]

    classDef project fill:#154360,color:#fff,stroke:#1a5276,stroke-width:3px
    classDef concept fill:#d6eaf8,color:#154360,stroke:#2874a6,stroke-width:2px
    classDef classes fill:#d5f5e3,color:#145a32,stroke:#239b56,stroke-width:2px
    classDef security fill:#fcf3cf,color:#7d6608,stroke:#b7950b,stroke-width:2px
    classDef methods fill:#e8daef,color:#512e5f,stroke:#8e44ad,stroke-width:2px
    classDef operations fill:#fadbd8,color:#78281f,stroke:#c0392b,stroke-width:2px

    class A project
    class B,C,D,E,F,G concept
    class H,I,J,K,U,V,W,X classes
    class N,O,P security
    class Q,R,S,T,L,M methods
    class Y,Z,AA,AB,AC operations
```
