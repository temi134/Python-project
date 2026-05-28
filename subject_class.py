class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_price(self):
        total = self.price * self.quantity
        print('the total price is', total)

    def display(self):
        print('product name is', self.name)
        print('price is', self.price)
        print('quantity is', self.quantity)


class Student:
    def __init__(self, name, maths, english, science):
        self.name = name
        self.maths = maths
        self.english = english
        self.science = science

    def total_marks(self):
        total = self.maths + self.english + self.science
        print('the total marks are', total)

    def percentage(self):
        total = self.maths + self.english + self.science
        percentage = (total / 300) * 100
        print('the percentage is', percentage)

    def display(self):
        print('student name is', self.name)
        print('maths marks are', self.maths)
        print('english marks are', self.english)
        print('science marks are', self.science)


product1 = Product('Laptop', 50000, 2)
product1.display()
product1.total_price()

student1 = Student('John', 85, 90, 88)
student1.display()
student1.total_marks()
student1.percentage()