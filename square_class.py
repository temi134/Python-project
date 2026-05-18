class square:
    def __init__(self,sides):
        self.sides = sides

    def areas(self):
        area = self.sides * self.sides
        print('the area is', area)

    def perimeters(self):
        perimeter = self.sides * 4
        print('the perimeter is', perimeter)

square1 = square(5)
square2 = square(15)

square1.areas()
square1.perimeters()
square2.areas()
square2.perimeters()

 