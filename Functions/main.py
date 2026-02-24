def cal_sum(n):
    sum = 0
    for i in range(n+1):
        sum += i

    return sum


n = int(input("Enter a number: "))
print("Sum of first", n, "numbers is:", cal_sum(n))



def greet():
    print("Hello, welcome to functions in Python!")

greet()
greet()
greet()



print("Built-In Functions")

print("Hello", end=" ")  # here end is used to avoid new line after printing "Hello" and instead it will print a space.
print("World!") # here no end means it will print a new line after printing "World!"



print("In-built Functions")



def cal_mul(a=1,b=1):
    return a*b

print(cal_mul(5,6)) # 30
print(cal_mul(5))   # 5, here b will take default value 1
print(cal_mul())    # 1, here both a and b will take default value
