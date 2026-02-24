arr = [1,2,3,4,6]
print(type(arr))
arr[4] = 5
arr.append(6)
print(arr)
print(len(arr))
arr.append("Bangalore")
print(arr)

arr[len(arr)-1] = 7
print("Element at last index:", arr[len(arr)-1])

arr.sort()
print("Sorted array: ", arr)

arr.sort(reverse=True)
print("Sorted array in reverse order: ", arr)

arr.reverse()
print("Reversed array: ", arr)

arr.insert(0,0)
print("Array after inserting 0 at index 0: ", arr)

arr.append(0)
arr.remove(0)
print("Array after removing first occurrence of 0: ", arr)

arr.pop(len(arr)-1)
print("Array after popping last element: ", arr)
