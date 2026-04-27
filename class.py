class Car:
    def __init__(self,colour,speed,type,brand):
        self.colour = colour
        self.speed = speed
        self.type = type
        self.brand = brand

    def display(self):
        print(self.colour+" "+ self.speed+" "+ self.type+" "+self.brand+" ")

car1 = Car("black","100","SUV","mercedes")
car1.display()
car2 = Car("white","140","Sports car","BMW")
car2.display()

