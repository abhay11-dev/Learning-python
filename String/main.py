str1 = "Hello world"
str2 = "Hello world and learner's"
str3 = 'Hello peoples"s'

print("str1 is: ",str1)
print("str2 is: ",str2)
print("str3 is: ",str3)


s1 = "Hello"
s2 = "World"
print("The concatenation of s1 and s2 is: ",s1 + s2) # concatenation is used to combine two strings. It will return "HelloWorld"
print("The concatenation of s1 and s2 is: ",s1 + " " + s2) # concatenation with space
print("Length of s1 is:",len(s1)) # len() function is used to find the length of the string. It will return 5

print("Indexing of 1st char in s1:",s1[0]) # indexing is used to access the individual characters of the string. It starts from 0. So s1[0] will return 'H'
# s1[0] = "h" # strings are immutable in Python. So we cannot change the value of a character in the string. It will give an error.
# print("String s1: ",s1) # s1 will remain unchanged as strings are immutable. It will print "Hello"

print("Slicing of s1 from index 0 to 3 is: ",s1[0:4]) # slicing is used to access a range of characters in the string. It will return 'Hell'
print("Slicing of s1 from index 2 to end is: ",s1[2:]) # slicing from index 2 to end will return 'llo'
print("Slicing of s1 from start to index 3 is: ",s1[:4]) # slicing from start to index 3 will return 'Hell'
print("Slicing of s1 with indexing is: ",s1[:]) # slicing with empty indexing will return 'Hello'
print("SLicing with negative indexing is: ",s1[-5:]) # slicing with negative indexing will return 'Hello'
print("Slicing with negative indexing is: ",s1[:-1]) # slicing with negative indexing will return 'Hell' as it will exclude the last character 'o'
print("Slicing of s1 with step 2 is: ",s1[0:5:2]) # slicing with step 2 will return 'Hlo'



print("Ends with 'o':",s1.endswith("o")) # endswith() function is used to check if the string ends with a specific character or not. It will return True if it ends with 'o' and False otherwise.
print("Starts with 'H':",s1.startswith("H")) # startswith() function is used to check if the string starts with a specific character or not. It will return True if it starts with 'H' and False otherwise.
print("Capitalized:",s1.capitalize()) # capitalize() function is used to convert the first character of the string to uppercase and the rest to lowercase. It will return 'Hello'
print("Uppercase:",s1.upper()) # upper() function is used to convert all the characters of the string to uppercase. It will return 'HELLO'
print("Lowercase:",s1.lower()) # lower() function is used to convert all the characters of the string  to lowercase. It will return 'hello'
print("Count of 'l' in s1 is: ",s1.count("l")) # count() function is used to count the number of occurrences of a specific character in the string. It will return 2 as there are 2 'l' in 'Hello'
print("Index of 'o' in s1 is: ",s1.index("o")) # index() function is used to find the index of the first occurrence of a specific character in the string. It will return 4 as 'o' is at index 4 in 'Hello'
print("Find index of 'o' in s1 is: ",s1.find("o")) # find() function is used to find the index of the first occurrence of a specific character in the string. It will return 4 as 'o' is at index 4 in 'Hello'
print("Replace 'o' with 'a' in s1 is: ",s1.replace("o","a")) # replace() function is used to replace a specific character in the string with another character. It will return 'Hella' as it will replace 'o' with 'a' in 'Hello'

