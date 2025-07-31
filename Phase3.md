# ✅ Phase 3: Class Variables and Class Methods

### 🎯 Goal: Understand shared data and class-level functionality in Python OOP.

---

## 🔹 Instance vs Class Variables

### ✅ What are Instance Variables?
- **Defined inside the constructor (`__init__()` method)** using `self`.
- **Unique for each object** (instance).
- Stored in the object’s namespace.
- Used to hold data **specific to that particular object**.

```python
class Student:
    def __init__(self, name, age):
        self.name = name            # instance variable
        self.age = age              # instance variable

s1 = Student("Ali", 20)
s2 = Student("Zara", 25)

print(s1.name)   # Ali
print(s2.name)   # Zara
```

### ✅ What are Class Variables?
- **Shared by all instances** of the class.
- Defined **outside of any method**, but inside the class body.
- Used to store **common data** for all objects.

```python
class Student:
    school_name = "Green Valley School"  # class variable

    def __init__(self, name):
        self.name = name                 # instance variable

s1 = Student("Ali")
s2 = Student("Zara")

print(s1.school_name)   # Green Valley School
print(s2.school_name)   # Green Valley School
```

✅ You can **access** class variables using:
- `ClassName.variable_name`
- `self.variable_name` (less preferred for clarity)

✅ You can **change** class variables using:
- `ClassName.variable_name = "NewValue"` ✅
- `self.variable_name = "NewValue"` ❌ (this creates an instance variable and hides the class variable for that object)

---

## 🔹 Declaring and Accessing

```python
class Product:
    tax_rate = 0.18  # Class Variable

    def __init__(self, name, price):
        self.name = name           # Instance Variable
        self.price = price

    def final_price(self):
        return self.price + (self.price * Product.tax_rate)

p1 = Product("Shirt", 1000)
p2 = Product("Shoes", 2000)

print(p1.final_price())  # 1180.0
print(p2.final_price())  # 2360.0
```

---

## 🔹 Class Methods

### ✅ What is a Class Method?
- A method that **works with the class itself**, not with the instance.
- Used when you want to access or modify **class-level data**.
- Decorated with `@classmethod`.
- Takes `cls` (not `self`) as the first parameter.

```python
class Employee:
    count = 0

    def __init__(self, name):
        self.name = name
        Employee.count += 1

    @classmethod
    def get_employee_count(cls):
        return cls.count

print(Employee.get_employee_count())  # 0
e1 = Employee("Ali")
e2 = Employee("Zara")
print(Employee.get_employee_count())  # 2
```

### ✅ Difference from Instance Methods:

| Feature          | Instance Method           | Class Method                 |
|------------------|---------------------------|------------------------------|
| First Parameter  | `self` (object reference) | `cls` (class reference)      |
| Access           | Can access instance data  | Can access class data        |
| Decorator        | None                      | `@classmethod`               |
| Called using     | object or class           | object or class              |

---

## 🔹 Use Cases of Class Methods
- Factory methods to create objects.
- Maintaining counters, stats.
- Loading from files/databases.
- Shared configuration.

### ✅ Example: Factory Method
```python
class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def from_string(cls, date_string):
        day, month, year = map(int, date_string.split('-'))
        return cls(day, month, year)

d = Date.from_string("31-12-2025")
print(d.day, d.month, d.year)  # 31 12 2025
```

---

## 🔹 Static Methods

### ✅ What is a Static Method?
- Does **not take self or cls** as the first parameter.
- **No access** to instance or class data.
- Defined using the `@staticmethod` decorator.
- Behaves like a regular function inside a class.
- Used for **utility/helper** functionality.

```python
class MathTools:
    @staticmethod
    def add(x, y):
        return x + y

print(MathTools.add(3, 5))  # 8
```

### ✅ When to Use Static Methods:
- The method performs a task that’s related to the class but doesn’t require access to instance or class variables.
- Clean organization of helper functions under related classes.

---

### ↺ Comparison: Instance vs Class vs Static Methods

| Method Type     | Decorator     | First Parameter | Access to Instance? | Access to Class? | Typical Use |
|-----------------|---------------|------------------|----------------------|------------------|-------------|
| Instance Method | None          | `self`           | ✅ Yes               | ✅ Yes           | Access object data |
| Class Method    | `@classmethod`| `cls`            | ❌ No                | ✅ Yes           | Class-level operations |
| Static Method   | `@staticmethod`| None            | ❌ No                | ❌ No            | Utility/helper functions |
