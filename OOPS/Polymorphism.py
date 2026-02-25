print(1+2) # Addition of numbers
print("Hello" +  " World") #Concatenation of strings
#Operaotor overloading is the ability to define different behaviors for an operator based on the types of operands. 
# In Python, we can achieve operator overloading by defining special methods in a class.


#dunder function
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

p1 = Point(1, 2)
p2 = Point(3, 4)
p3 = p1 + p2  # This will call the __add__ method
print(f"Result of adding points: ({p3.x}, {p3.y})")