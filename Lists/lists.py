"""
so far a variable stores one value at a time. But what if you need to store the marks of 5 students or the name of 10 cities creating a separate variable for each one quickly becomes messy and impractical. A list solves this it is a collection that stores multiple values if a single variable kept in specific order
"""

students = ["Rahul", "Shibram","Karan", 34, 999.45, True, "SAnjay"]
#its mutable
# its ordered
# allows duplicate
# any data type it can store any data type
print(students)


names = ["Ak", "Vijay", "Nasleen",44,True, False]
print(type(names))
marks = [3,7,88,98]
#operations

print(marks * 4) # it only creates duplicating the numbers you just mentioned
# print(marks + 4)
# print(marks / 4) these both dont work

print(names + marks)