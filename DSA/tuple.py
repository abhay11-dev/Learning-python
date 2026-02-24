arr = (0,2,3,4,5,6,7,8,9) #Tuple is immutable, it cannot be changed after creation
print(type(arr))
print(arr)

# arr[0] = 1 #Not allowed, Tuple item do not support assignment



#Palindrome check using tuple
brr = arr.copy()
brr.reverse()
if arr == brr:
    print("Palindrome")
else:
    print("Not Palindrome")