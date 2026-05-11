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

class Bike:
    def __init__(self, colour, speed, brand, engine):
        self.colour = colour
        self.speed = speed
        self.brand = brand
        self.engine = engine

    def display(self):
        print(self.colour + " " + self.speed + " " + self.brand + " " + self.engine + " ")


bike1 = Bike("red", "180", "Yamaha", "600cc")
bike1.display()

bike2 = Bike("blue", "200", "Kawasaki", "1000cc")
bike2.display()


class Plane:
    def __init__(self, colour, speed, company, model):
        self.colour = colour
        self.speed = speed
        self.company = company
        self.model = model

    def display(self):
        print(self.colour + " " + self.speed + " " + self.company + " " + self.model + " ")


plane1 = Plane("white", "900", "Boeing", "747")
plane1.display()

plane2 = Plane("silver", "850", "Airbus", "A320")
plane2.display()