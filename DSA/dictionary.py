dict = { 
    "name" : "Abhay",
    "age" : 20,
    "course" : "B.Tech",
    "subjects" : ["DSA", "Python", "Maths"],
    "organization" : "Lovely Professional University"
}

print(type(dict))

print(dict)
print(dict["name"])

print(dict["subjects"])
print(dict["subjects"][0])

dict["organization"] = "Affinsys"
dict["location"] = "Bangalore"
print(dict)




students = {
    "student1" : {
        "name" : "Abhay",
        "age" : 20,
        "course" : "B.Tech"
    },
    "student2" : {
        "name" : "Rahul",
        "age" : 21,
        "course" : "B.Tech"
    }
}

print(students)
print(students["student1"])
print(students["student1"]["name"])


print(students.keys()) #Returns a view object that displays a list of all the keys in the dictionary
print(students.values()) #Returns a view object that displays a list of all the values in the dictionary
print(students.items()) #Returns a view object that displays a list of dictionary's key-value tuple pairs
print(list(students.items())) #Returns a view object that displays a list of dictionary's key-value list pairs

print(students.get("student1")) #Returns the value of the specified key else none
print(students["student1"]) #Returns the value of the specified key else error

print(students.get("student3")) #Returns the value of the specified key else none
# print(students["student3"]) #Returns the value of the specified key else error

new_student = {"student3" : {
    "name" : "Rahul",   
    "age" : 21,
    "course" : "B.Tech"
    }}

students.update(new_student) #Updates the dictionary with the key-value pairs from new_student
print(students)
