class car:
    def __init__(self, color, speed):
        self.color=color
        self.speed=speed
    def drive(self):
        print(f"The information{self.color},{self.speed}")

d1=car("red",150)
d2=car("red",1550)
d3=car("red",15540)
d4=car("red",154440)

d1.drive()
d2.drive()
d3.drive()
d4.drive()

