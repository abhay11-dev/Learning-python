n = 0
while(n<=5):
    print(n)
    n += 1

print("Done")

arr = [1,4,9,16,25,36,49,64,81,100]
i = 0
while(i<len(arr)):
    print(arr[i])
    i += 1


tup = (1,4,9,16,25,36,49,64,81,100)
i=0
x = int(input("Enter a number to search: "))

while(i<len(tup)):
    if(tup[i]==x):
        print("Found")
        break
    else:
        i += 1
else:
    print("Out of loop")


if(i==len(tup)):
    print("Not Found")




list = [1,2,3,4,5,6,7,8,9,10]
for i in list:
    print(i)

print("for loop Done")

tup = (1,4,9,16,25,36,49,64,81,100)
for i in tup:
    print(i)
else:
    print("Done")


for i in list:
    if(i==5):
        print("Found")
        break
else:
    print("Not Found")



print("Range function")
print("Range with one argument: Stop only")
for val in range(10):
    print(val)

print("Range with two arguments: Start and Stop")
for val in range(1,11):
    print(val)

print("Range with three arguments: Start, Stop and Step")
for val in range(1,11,2):
    print(val)


print("Pass statement")
for i in range(10):
    pass

print("Passed the loop")