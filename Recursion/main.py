def show(n):
    if(n==0):
        return
    print(n , end=" ")
    show(n-1)
    print("\nHello",n,end=" ")

n = int(input("Enter a number: "))
show(n)




def cal_sum(n):
    if(n==0):
        return 0
    return n + cal_sum(n-1)

print("Sum of first", n, "numbers is:", cal_sum(n))