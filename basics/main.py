print("hello world") # print is a function here 
print("My name is Abhay")
print("I am learning Python", "& My age is 20") # comma is used to separate the values and it will print space between them.
print("I am learning Python", "\nMy age is",20) # \n is used to print in new line
print("I am learning Python", "\tMy age is",20) # \t is used to print in tab space


name = "Abhay"
age = 20
price = 11.11

print("My name is", name, "and my age is", age) # we can also use variables in print statement

print("The data type of name is: ",type(name))
print("The data type of age is: ",type(age))
print("The data type of price is: ",type(price))
 # type() function is used to check the data type of the variable


name1 = "abhay"
name2 = 'abhay'
name3 = """abhay"""
name4 = '''abhay'''
print("name1 is: ",name1)
print("name2 is: ",name2)
print("name3 is: ",name3)
print("name4 is: ",name4)


isValid = True
isValid2 = False
print("The value of isValid is: ",isValid)
print("The value of isValid2 is: ",isValid2)

unknown = None
print("The value of unknown is: ",unknown)

print("The data types are: ",type(isValid), type(isValid2) ,type(unknown))



a = 2
b = 3
print("The result of a + b is: ",a + b) # addition
print("The result of a - b is: ",a - b) # subtraction
print("The result of a * b is: ",a * b) # multiplication
print("The result of a / b is: ",a / b) # division
print("The result of a % b is: ",a % b) # modulus
print("The result of a ** b is: ",a ** b) # exponentiation

print("The result of a == b is: ",a == b) # == is used to check if the values of a and b are equal or not. It will return True if they are equal and False if they are not equal.
print("The result of a != b is: ",a != b) # != is used to check if the values of a and b are not equal or not. It will return True if they are not equal and False if they are equal.
print("The result of a >= b is: ",a >= b) # >= is used to check if the value of a is greater than or equal to the value of b. It will return True if a is greater than or equal to b and False otherwise.
print("The result of a <= b is: ",a <= b) # <= is used to check if the value of a is less than or equal to the value of b. It will return True if a is less than or equal to b and False otherwise.
print("The result of a > b is: ",a > b) # > is used to check if the value of a is greater than the value of b. It will return True if a is greater than b and False otherwise.
print("The result of a < b is: ",a < b) # < is used to check if the value of a is less than the value of b. It will return True if a is less than b and False otherwise.

a *= 2 # a = a * 2
a += 3 # a = a + 3
a -= 1 # a = a - 1
a /= 2 # a = a / 2
a %= 3 # a = a % 3
a **= 2 # a = a ** 2

print("The answer of not of a==b is: ",not (a==b)) # not is used to negate the value of a boolean variable. It will return False if the value is True and True if the value is False.

c = True
d = False
print("The result of c and d is: ",c and d) # and is used to check if both the values are True. It will return True if both the values are True and False otherwise.
print("The result of c or d is: ",c or d) # or is used to check if at least one of the values is True. It will return True if at least one of the values is True and False otherwise.



"""
    This is a multi-line comment in Python. It is used to write comments that span multiple lines.
    It is enclosed within triple quotes (""" """) or triple single quotes (''' ''').
"""