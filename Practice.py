class personal:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def greet(self):
        print(f"Hello, my name is {self.name} and i am {self.age} years old")
    
personal1 = personal("ali",24)
personal1.greet()

personal1 = personal("ahmad",24)
personal1.greet()
personal1 = personal("nawaz",24)
personal1.greet()
personal1 = personal("sabtan",24)
personal1.greet()
