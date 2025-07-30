
class Mobile:
    def __init__(self,brand,price): #A constructor method
        self.brand=brand
        self.price=price

    def show_info(self):
        print(f"the brand name is {self.brand},and price is {self.price}")
    
brand_info = Mobile("nokia",234)
brand_info.show_info()



class Mobile:
    def mobile_info(self,brand,price):
        self.brand=brand
        self.price=price
    def show_info(self):
        print(f"the brand name is {self.brand},and price is {self.price}")
m1= Mobile()
m1.mobile_info("NOkia",45)
m1.show_info()

class Student:
    def __init__(self, name):
        self.name = name

s1 = Student("Ali")
s1 = Student("Zara")

print(s1.name)  # Ali
print(s1.name)  # Zara
