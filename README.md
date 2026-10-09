<div align="center">
<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=800&size=28&duration=3000&pause=1000&color=FF0000&center=true&vCenter=true&width=1000&lines=%F0%9F%9A%80+OOP+WRAPPER+%7C+EMPLOYEE+MANAGEMENT+SYSTEM+%F0%9F%9A%80" alt="OOP Wrapper | Employee Management System" />
</div>

<div align="center">


### ✨ Object-Oriented Programming with Python ✨

**A Python project demonstrating OOP concepts through an Employee Management System.**

<br>

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![OOP](https://img.shields.io/badge/Object--Oriented-Programming-8E44AD?style=for-the-badge)
![Status](https://img.shields.io/badge/Project-Completed-2E8B57?style=for-the-badge)

</div>

---

## 🌟 About the Project

**OOP Wrapper** is a Python project designed to demonstrate the practical implementation of Object-Oriented Programming (OOP) concepts.

The project uses different classes to represent people, employees, managers, and developers. It demonstrates how classes, inheritance, encapsulation, and polymorphism can be used to organize and manage employee information.

### 🎯 Project Objectives

- Understand the fundamentals of Object-Oriented Programming.
- Implement classes, objects, and constructors.
- Demonstrate inheritance and method overriding.
- Protect employee information using encapsulation.
- Perform employee management operations.

---

## ✨ Key Features

<table>
<tr>
<td width="50%">

### 👤 Class-Based Design
Organizes information using classes and objects.

</td>
<td width="50%">

### 🧬 Inheritance
Reuses employee properties and methods.

</td>
</tr>
<tr>
<td width="50%">

### 🔐 Encapsulation
Uses private attributes with getter and setter methods.

</td>
<td width="50%">

### 🎭 Polymorphism
Demonstrates method overriding through `display()`.

</td>
</tr>
<tr>
<td width="50%">

### ✏️ Employee Updates
Updates employee salary using an employee ID.

</td>
<td width="50%">

### 🗑️ Employee Removal
Removes an employee record using an employee ID.

</td>
</tr>
</table>

---

## 🏗️ Class Structure

| Class | Responsibility |
|:---|:---|
| 👤 `Person` | Stores basic information such as name and age. |
| 💼 `Employee` | Extends Person and manages employee-specific information. |
| 👨‍💼 `Manager` | Extends Employee with manager-specific information, such as department. |
| 👩‍💻 `Developer` | Extends Employee with developer-specific information, such as programming language. |

### 🔗 Class Relationships

- `Employee` inherits from `Person`.
- `Manager` inherits from `Employee`.
- `Developer` inherits from `Employee`.

This structure demonstrates code reusability and hierarchical relationships between classes.

---

## 🧠 OOP Concepts Implemented

<details>
<summary><b>📦 1. Classes and Objects</b></summary>

<br>

Classes define the structure and behaviour of objects. Objects represent individual instances of these classes.

**Used in:** `Person`, `Employee`, `Manager`, and `Developer`.

</details>

<details>
<summary><b>🔐 2. Encapsulation</b></summary>

<br>

Encapsulation protects data by controlling access to attributes.

**Implemented using:**
- Private attributes for employee ID and salary.
- Getter methods to retrieve values.
- Setter methods to update values.

</details>

<details>
<summary><b>🧬 3. Inheritance</b></summary>

<br>

Inheritance allows a class to reuse properties and methods from another class.

**Implemented using:**
- `Employee` inheriting from `Person`.
- `Manager` inheriting from `Employee`.
- `Developer` inheriting from `Employee`.

</details>

<details>
<summary><b>🎭 4. Polymorphism</b></summary>

<br>

Polymorphism allows methods with the same name to behave differently in different classes.

**Implemented using:** Method overriding with the `display()` method.

</details>

<details>
<summary><b>🏗️ 5. Constructors and super()</b></summary>

<br>

Constructors initialize object attributes. The `super()` function is used to access parent-class functionality.

The project also demonstrates a constructor overloading pattern using `*args`, if implemented in the constructor.

</details>

<details>
<summary><b>🔍 6. isinstance() and issubclass()</b></summary>

<br>

- `isinstance()` checks whether an object belongs to a class or its subclass.
- `issubclass()` checks whether one class inherits from another class.

</details>

---

## ⚙️ Project Working

The project follows an organized process to create and manage employee objects.

| Step | Operation | Description |
|:---:|:---|:---|
| 01 | 🏁 Initialization | Start the program and prepare the required objects. |
| 02 | 👤 Object Creation | Create objects from the defined classes. |
| 03 | 📝 Attribute Initialization | Initialize personal and employee information. |
| 04 | 🖥️ Display Details | Display information using class methods. |
| 05 | ✏️ Update Salary | Update an employee's salary using their ID. |
| 06 | 🗑️ Remove Employee | Remove an employee record using their ID. |
| 07 | 🚪 Exit | Close resources and terminate the program. |

---

## 🛠️ Technologies Used

<div align="center">

| Technology | Purpose |
|:---|:---|
| 🐍 Python | Main programming language |
| 🧩 OOP | Classes, objects, inheritance, and polymorphism |
| 🗂️ GitHub | Project hosting and documentation |

</div>

---


## 🎓 Learning Outcomes

Through this project, I practised:

- Designing classes and creating objects.
- Understanding parent-child class relationships.
- Applying encapsulation to protect attributes.
- Implementing method overriding.
- Using constructors and `super()`.
- Managing employee information through Python code.

---


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
<h1 align="center">📸 OUTPUT</h1>

<p align="center">
          
<img width="1878" height="7807" alt="op 5 ss" src="https://github.com/user-attachments/assets/80d97bc3-4e02-4a2d-ace8-70d4b29fe7f3" />


 </p>
 
<h1 align="center">📸 video demo</h1>

<p align="center">


https://github.com/user-attachments/assets/cdc5fd3c-ed62-435c-a383-d2d8e685a618

</p>



## 💜 Thank You for Visiting!

**OOP Wrapper — Learning Python Through Practical Implementation**

*Built with Python 🐍 and a passion for learning.*
<h2 align="center">
  ✨ Created by Khushi Chaudhary ✨
</h2>
<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Poppins&weight=600&size=24&pause=1000&color=FF69B4&center=true&vCenter=true&width=500&lines=Author+%3A+Khushi+Chaudhary;Python+Developer;OOP+wrapper+Project" alt="Typing SVG" />
</p>
</div>


