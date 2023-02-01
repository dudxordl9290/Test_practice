class Circle():

    pii = 3.14

    def __init__(self,radius=1):
        self.radius = radius

    def area(self):

        result = self.radius**2
        result = result*self.pii

        return result
    
    def perimeter(self):
        return 2*self.radius*self.pii

mycircle = Circle(radius=4)
print(mycircle.area())
print(mycircle.perimeter())