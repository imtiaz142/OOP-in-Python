"""
Encapsulation in Python
-----------------------
Encapsulation means "hiding data" and providing controlled access
through methods like Getters and Setters.
"""

# ------------------------------------------------------------
# 1. PUBLIC VARIABLE EXAMPLE (No Encapsulation)
# ------------------------------------------------------------
class FanPublic:
    def __init__(self, speed):
        # Public variable (anyone can access/change it)
        self.speed = speed

# Usage
fan1 = FanPublic(3)
print("\n--- Public Variable Example ---")
print("Initial Speed:", fan1.speed)   # Can access directly
fan1.speed = -5                       # Can set invalid data (NO CONTROL)
print("Invalid Speed Set:", fan1.speed)


# ------------------------------------------------------------
# 2. PRIVATE VARIABLE WITH GETTER AND SETTER (Encapsulation)
# ------------------------------------------------------------
class FanPrivate:
    def __init__(self, speed):
        # Private variable (cannot be accessed directly)
        self.__speed = speed

    # Getter (read the private variable)
    def get_speed(self):
        return self.__speed

    # Setter (update the private variable with validation)
    def set_speed(self, speed):
        # Condition ensures safe values
        if 0 <= speed <= 5:
            self.__speed = speed
            print(f"Speed set to {speed}")
        else:
            print("❌ Invalid speed! Must be between 0 and 5.")

# Usage
fan2 = FanPrivate(3)
print("\n--- Private Variable Example ---")
print("Initial Speed:", fan2.get_speed())  # Access via getter
fan2.set_speed(4)                          # Valid update
fan2.set_speed(10)                         # Invalid update


# ------------------------------------------------------------
# 3. REAL-WORLD EXAMPLE: BANK ACCOUNT
# ------------------------------------------------------------
class BankAccount:
    def __init__(self, holder, balance):
        self.holder = holder      # Public
        self.__balance = balance  # Private

    # Getter: Check balance
    def get_balance(self):
        return self.__balance

    # Setter-like methods (Encapsulation in action)
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"✅ Deposited ${amount}. New Balance: ${self.__balance}")
        else:
            print("❌ Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"✅ Withdrew ${amount}. Remaining Balance: ${self.__balance}")
        else:
            print("❌ Insufficient funds or invalid amount.")

# Usage
account = BankAccount("Ali", 1000)
print("\n--- Bank Account Example ---")
print("Account Holder:", account.holder)
print("Balance:", account.get_balance())   # Access via getter
account.deposit(500)
account.withdraw(300)
account.withdraw(2000)                     # Invalid


# ------------------------------------------------------------
# 4. ADVANCED: WHAT ELSE CAN A SETTER DO?
# ------------------------------------------------------------
class Device:
    def __init__(self, temperature):
        self.__temperature = temperature

    # Setter adjusts and triggers extra behavior
    def set_temperature(self, temp):
        if temp > 40:
            print("⚠️ Warning: Overheating!")
            self.__temperature = 40   # Auto-adjust
        elif temp < 0:
            print("⚠️ Too cold! Auto-adjusting to 0.")
            self.__temperature = 0
        else:
            self.__temperature = temp
        print(f"Temperature set to {self.__temperature}°C")

    # Getter
    def get_temperature(self):
        return self.__temperature

# Usage
device = Device(25)
print("\n--- Advanced Setter Example ---")
device.set_temperature(45)   # Auto-adjusts + Warning
device.set_temperature(-10)  # Auto-adjusts + Warning
device.set_temperature(30)   # Normal
