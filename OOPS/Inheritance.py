class Bank:
    def __init__(self,acc_no,acc_pass):
        self.__acc_no = acc_no
        self.acc_pass = acc_pass

    def get_acc_no(self):
        return self.__acc_no

    def __salary(self):
        print("This is a private method")


b1 = Bank("123456789","abc123")
print(b1.get_acc_no())  # Accessing private variable using getter method
print(b1.acc_pass)  # Accessing public variable directly

b1.__acc_no = "987654321"  # Attempting to modify private variable directly
print(b1.get_acc_no())  # The private variable remains unchanged

# b1.__salary()  # Attempting to call private method directly (will raise an error)






print("\n-----------------------------\n")
class Bike:
    color = "Battalion Black"
    @staticmethod
    def start():
        print("Bike started")

    @staticmethod
    def stop():
        print("Bike stopped")


class Bullet(Bike):
    def __init__(self,name):
        self.name = name


b1 = Bullet("Royal Enfield")
b1.start()  # Calling static method from parent class
b1.stop()   # Calling static method from parent class
print(f"Bike name: {b1.name} with color {b1.color}")  # Accessing instance variable from child class
        


print("\n-----------------------------\n")


class Car:
    @staticmethod
    def start():
        print("Car started")

    @staticmethod
    def stop():
        print("Car stopped")


class Toyota(Car):
    
    @staticmethod
    def first_base():
        print("This is the first base method")


class Fortuner(Toyota):
    
    @staticmethod
    def second_base():
        print("This is the second base method")


c1 = Fortuner()
c1.start()  # Calling static method from grandparent class
c1.stop()   # Calling static method from grandparent class
c1.first_base()  # Calling method from parent class
c1.second_base()  # Calling method from child class



print("\n-----------------------------\n")

class Father:

    @staticmethod
    def father_method():
        print("This is the father method")


class Mother:
    @staticmethod
    def mother_method():
        print("This is the mother method")

    
class Child(Father, Mother):
    @staticmethod
    def child_method():
        print("This is the child method")

c1 = Child()
c1.father_method()  # Calling method from Father class
c1.mother_method()  # Calling method from Mother class
c1.child_method()   # Calling method from Child class

print("\n-----------------------------\n")


class A:
    def __init__(self,type):
        self.type = type
        print("This is class A")

class B(A):
    def __init__(self,type):
        super().__init__(type)
        print("This is class B")

b1 = B("Example Type")
print(f"Type: {b1.type}")  # Accessing instance variable from parent class


print("\n-----------------------------\n")


class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")
    
    @property
    def percentage(self):
        return (self.age / 100) * 100  # Just a dummy calculation for percentage
    
s1 = Student("Alice", 20)
s1.display_info()
print(f"Percentage: {s1.percentage}%")  # Accessing percentage as a property
s1.age = 25  # Modifying age
print(f"Updated Percentage: {s1.percentage}%")  # Accessing updated percentage as a property