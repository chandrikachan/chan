class Rectangle():
    def __init__(self, l, w):
        self.length = l
        self.width  = w
    def rectangle_area(self):
        return self.length*self.width
class square:
    def areaOfSquare(self, s):
        return s*s
newRectangle = Rectangle(15, 10)
print("this is the area of rectangle is",newRectangle.rectangle_area())
print("Enter the Side Length of Square: ", end="")
l = float(input())
obj = square()
a = obj.areaOfSquare(l)
print("\nArea = {:.2f}".format(a))
import math as M #area of circle 
Radius = float (input ("Please enter the radius of the given circle: "))  
area_of_the_circle = M.pi* Radius * Radius  
print (" The area of the given circle is: ", area_of_the_circle) 



