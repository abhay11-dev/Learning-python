class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def greet():
        print("Hello, welcome to the class!")

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")


student1 = Student("Alice", 20)
student1.display_info()
student1.greet()

student2 = Student("Bob", 22)
student2.display_info()
student2.greet()



