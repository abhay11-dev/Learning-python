num = int(input("Enter a number: "))

if(num>18):
    print("You are eligible to vote.")
elif(num==18):
    print("You are eligible to vote but you need to wait for a year.")
else:
    print("You are not eligible to vote.")

