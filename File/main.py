# f = open("file.txt", "r")

# # print(f.read()) # reads the entire file
# print(f.readline()) # reads the next line
# print(f.readline()) # reads the next line
# print(f.read())

# f.close()



f2 = open("file.txt", "w") # opens the file in write mode
f2.write("This is a new line.\n")
f2.close()

f3 = open("file.txt", "r") # opens the file in append mode
print(f3.read())
f3.close()


f4 = open("file.txt", "a") # opens the file in append mode
f4.write("This is another new line.")
f4.close()

f5 = open("file.txt", "r") # opens the file in append mode
print(f5.read())
f5.close()