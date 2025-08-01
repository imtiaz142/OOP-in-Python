# 🔒 Encapsulation in Python - Complete Beginner Guide

## 📘 What is Encapsulation?
Encapsulation is a fundamental concept in object-oriented programming (OOP) where **data (variables)** and **methods (functions)** that operate on the data are bundled together into a single unit, known as a **class**.

It also means **restricting direct access** to some of an object's components, which is called **data hiding**.

---

## 💊 Real-life Analogy
**Think of a medicine capsule**:
- The capsule wraps all the ingredients inside.
- You don’t directly access the ingredients; they’re protected.
- You take the capsule, and it works as intended.

Just like that, in programming:
- A class wraps both data and logic.
- You hide sensitive data from outside access.
- Only expose what’s necessary using special methods.

---

## 💡 Why is Encapsulation Important?
Encapsulation provides:
- ✅ **Security**: Prevents outside code from messing with internal data.
- 🔧 **Control**: Allows controlled access to internal data.
- 🔄 **Flexibility**: Makes it easier to modify or extend code.
- 📦 **Maintainability**: Keeps code clean and manageable.

---

## ⚙️ How Encapsulation Works in Python

### 🔐 1. Data Hiding (Public vs. Private Members)
```python
class Employee:
    def __init__(self, name, salary):
        self.name = name          # Public member
        self.__salary = salary    # Private member
```

- `self.name` is **public**: accessible from outside the class.
- `self.__salary` is **private**: can't be accessed directly.

### 🚫 Accessing Private Member Directly (Not Recommended)
```python
emp = Employee("Ali", 50000)
print(emp.name)         # ✅ Works
print(emp.__salary)     # ❌ Error: AttributeError
```

---

### 🧰 2. Getters and Setters
To **access or modify private data safely**, we use:
- **Getter** methods to read data.
- **Setter** methods to write/update data.

```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def set_salary(self, new_salary):
        if new_salary > 0:
            self.__salary = new_salary
        else:
            print("❌ Invalid salary!")

emp = Employee("Ali", 50000)
print(emp.get_salary())
emp.set_salary(55000)
print(emp.get_salary())
emp.set_salary(-1000)  # Triggers validation
```

---

## 🧪 Step-by-Step Example

### ❌ Without Encapsulation
```python
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

s = Student("Ahmed", 90)
s.marks = -20    # ❌ No protection — logic error
```

### ✅ With Encapsulation
```python
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks

    def get_marks(self):
        return self.__marks

    def set_marks(self, value):
        if 0 <= value <= 100:
            self.__marks = value
        else:
            print("❌ Invalid marks. Must be between 0 and 100.")

s = Student("Ahmed", 90)
print(s.get_marks())        # ✅ 90
s.set_marks(95)             # ✅
print(s.get_marks())        # ✅ 95
s.set_marks(-10)            # ❌ Invalid
```

---

## 🏦 Full BankAccount Example Using Encapsulation
```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance   # Private member

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"✅ Deposited ${amount}")
        else:
            print("❌ Deposit amount must be positive")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"✅ Withdrew ${amount}")
        else:
            print("❌ Invalid withdrawal amount or insufficient funds")

    def get_balance(self):
        return self.__balance

# Using the class
acc = BankAccount("Imtiaz", 1000)
print(acc.get_balance())    # ✅ 1000
acc.deposit(500)            # ✅ Deposited
acc.withdraw(200)           # ✅ Withdrew
acc.withdraw(2000)          # ❌ Not enough balance
acc.deposit(-50)            # ❌ Invalid deposit
print(acc.get_balance())    # ✅ Updated balance
```

---

## 🎁 Benefits of Encapsulation

| Benefit       | Explanation                                                        |
|---------------|--------------------------------------------------------------------|
| 🔐 Security    | Prevents unintended access to internal variables                   |
| 🔧 Flexibility | You can change internal code without affecting outside code        |
| 📦 Maintainability | Organized structure makes your code cleaner and easier to debug |

---

## ⚠️ Common Mistakes by Beginners

### 1. ❌ Exposing All Data as Public
```python
class Person:
    def __init__(self, age):
        self.age = age  # No restriction
```
🔍 Anyone can assign invalid values: `person.age = -5`

### ✅ Use Encapsulation Instead
```python
class Person:
    def __init__(self, age):
        self.__age = age

    def get_age(self):
        return self.__age

    def set_age(self, new_age):
        if new_age >= 0:
            self.__age = new_age
        else:
            print("❌ Age cannot be negative")
```

### 2. ❌ Not Using Getters/Setters
If you always access data directly, you lose the chance to validate and protect it.

Use getter/setter methods to control how data is accessed or updated.

---

## ✅ Summary
| Term        | Meaning                                   |
|-------------|-------------------------------------------|
| Encapsulation | Hiding internal data and exposing only safe methods |
| Public       | Accessible from outside                   |
| Private      | Hidden using `__` prefix                  |
| Getter       | Method to read private data               |
| Setter       | Method to update private data             |

Encapsulation makes your programs **safer, more flexible, and easier to maintain**.

---

Would you like to practice by creating your own encapsulated class like `Car`, `LibraryBook`, or `UserProfile`? Feel free to ask!
