collection1 = {1,2,3,4,5,6,1,2,3,4,5,6} #Set is unordered collection of unique items
print(type(collection1))
print(collection1)

collection1.add(7) #Adds an element to the set
print(collection1)

collection1.remove(1) #Removes an element from the set, raises error if element not found
print(collection1)

collection2 = set() #Creates an empty set, cannot use set = {} as it creates an empty dictionary
print(type(collection2))


collection1.pop() #Removes and returns an arbitrary set element, raises error if set is empty
print(collection1)

collection1.clear() #Removes all elements from the set
print(collection1)




collection3 = {1,2,3,4,5}
collection4 = {4,5,6,7,8}

print(collection3.union(collection4)) #Returns a new set containing all elements from both sets
print(collection3.intersection(collection4)) #Returns a new set containing only elements that are common
print(collection3.difference(collection4)) #Returns a new set containing only elements that are in the first set but not in the second set
print(collection4.difference(collection3)) #Returns a new set containing only elements that are in the second set but not in the first set
print(collection3.symmetric_difference(collection4)) #Returns a new set containing only elements that are in either set but not in both sets (Union - Intersection)


