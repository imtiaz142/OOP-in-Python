# ✅ Phase 2: Creating Your First Class

### 🌟 **Goal:** Learn the basic syntax of a class and how to use it.

---

## 🔹 Creating a Simple Class

### What is a Class?
A **class** is a blueprint or template for creating objects (real-life entities). It defines the structure (data) and behavior (functions) of those objects.

---

### 📌 `class` keyword

- In Python, you define a class using the `class` keyword.
- Syntax:
```python
class ClassName:
    # attributes and methods go here
```

✅ Example:
```python
class Car:
    pass
```

🔍 Explanation:
- `Car` is the name of the class.
- `pass` is a placeholder. The class is currently empty.

---

## 🔹 Defining Attributes and Methods

### ➞ Attributes
- These are variables that **belong to the object**.
- Also called **instance variables**.

### ➞ Methods
- These are **functions defined inside a class**.
- They define **behavior** of the objects.

✅ Example:
```python
class Car:
    def __init__(self, brand, color):
        self.brand = brand      # attribute
        self.color = color      # attribute

    def drive(self):            # method
        print(f"{self.brand} car is driving")
```

🔍 Explanation:
- `__init__` is a special method called a **constructor**.
- `self.brand` and `self.color` are attributes.
- `drive()` is a method that performs an action.

---

## 🔹 Creating and Using Objects

### ✅ Instantiating an Object

- Creating an object means making a real instance of the class.

✅ Example:
```python
my_car = Car("Toyota", "Red")
```

🔍 Explanation:
- `my_car` is an object.
- `"Toyota"` and `"Red"` are passed as values to the constructor.

---

### ✅ Accessing Attributes and Methods

You can use dot notation (`object.attribute` or `object.method()`) to access properties and actions.

✅ Example:
```python
print(my_car.color)   # Output: Red
my_car.drive()        # Output: Toyota car is driving
```

---

## 🔹 Understanding `self` Keyword

### ✅ What is `self`?

- `self` is a reference to the current object.
- It lets the object refer to its own data and methods.
- You must include it as the first parameter in all instance methods (including `__init__`).

✅ Example:
```python
class Person:
    def __init__(self, name):
        self.name = name  # refers to the object's name attribute

    def greet(self):
        print(f"Hello, I am {self.name}")
```

### ✅ Why is it used?

- Without `self`, Python wouldn't know you're talking about the object's own data.

---

### ✅ Common Mistakes Beginners Make:

❌ Forgetting `self` in method definition:
```python
def greet():  # WRONG
    print("Hi")
```

✅ Correct:
```python
def greet(self):  # RIGHT
    print("Hi")
```

❌ Using `self` as a regular variable:
```python
self = "Ali"  # WRONG — self is not a value holder
```

---

## 🔹 Constructor Method `__init__()`

### ✅ What is a Constructor?

- A **constructor** is a special method called **automatically** when you create an object.
- In Python, it's defined with `__init__()`.

✅ Example:
```python
class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
```

🔍 Explanation:
- This constructor sets `name` and `roll_no` when the object is created.

---

### ✅ Default vs Parameterized Constructor

#### ➞ Default Constructor
A constructor with no parameters other than `self`.

```python
class Hello:
    def __init__(self):
        print("This is a default constructor")

h = Hello()  # Output: This is a default constructor
```

#### ➞ Parameterized Constructor
Takes additional arguments during object creation.

```python
class Student:
    def __init__(self, name):
        self.name = name

s = Student("Ali")
```

---

## 🔹 Instance Variables vs Local Variables

### ✅ Instance Variables

- Belong to **objects**
- Defined using `self`
- Exist as long as the object exists

```python
self.name = name  # instance variable
```

### ✅ Local Variables

- Exist only inside a method
- Not prefixed by `self`
- Disappear once the function finishes

```python
def set_name(self, name):
    new_name = name  # local variable
```

---

### ✅ Scope and Lifetime

#### ➞ Scope
- **Instance variables**: Accessible from any method inside the class using `self`.
- **Local variables**: Accessible only inside the function/method they are created in.

#### ➞ Lifetime
- **Instance variables**: Live as long as the object exists.
- **Local variables**: Die as soon as the function ends.

✅ Example:
```python
class Dog:
    def __init__(self, name):
        self.name = name  # instance variable

    def say_name(self):
        greeting = "Woof!"  # local variable
        print(f"{self.name} says {greeting}")
```

---
