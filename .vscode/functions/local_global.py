# scope
#global variables
name = "rahul"

def greet():
    #local variables
    message = "Hello" # i can not use this variable outside this function because it is declared as local and it is only can be accessible inside the function scope

    print(f"{message} {name}")

# print(message)
print(name)
greet()


count  = 0
def increase():
    global count
    #when i actually want to change the or access the variable as golbal 
    count  += 1;
    print(f"Inside funtion count = {count}")

increase()
increase()
print(f"Outside fucntion count = {count}")