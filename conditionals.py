# if statements
marks = 55
if marks >= 60 and marks <= 100:
    print("You have passed the exam")
else:
    print("You have failed the exam")

# indentation is not optional in python, it is mandatory to use indentaion in python. Indentation is used to define the block of code. In other programming languages, we use curly braces to define the block of code. In python, we use indentation to define the block of code.

if marks >= 60:
    print("Grade A")
elif marks >= 50:
    print("Grade B")
else:
    print("Grade C")


#by default  there are break in every elif statement, if you want to check all the conditions then you can use if statement instead of elif statement. In that case, all the conditions will be checked and all the blocks of code will be executed.

#nested if else
age = 45
certificate = True
# if age >= 18:
#     pass
# else:
#     print("Cannot hire, age is less than 18")

if age >= 18:
    if certificate:
        print("You are eligible to hire")
    else:
        print("Cannot hire, you don't have a certificate")
else:
    print("Cannot hire, age is less than 18")

status = "Adult" if age >= 18 else "Minor"
print(f"User is an {status}")