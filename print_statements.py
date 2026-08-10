name = "Anirudh"
age = 23
gender = "Male"
print("Hello",name,"your age is", age,"and your gender is", gender)
print("Hello "+name+"Your age is "+str(age)+"and your gender is "+gender)


print(name,age,gender,sep = " | ")
print(name,end = " ")
print(age)
print(gender,name,age,sep = " ",end = " ");


#F strings, formatting strings in python
print(f"Your name is {name}, your age is {age+30} and your gender is {gender}")