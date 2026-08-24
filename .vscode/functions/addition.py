def greet(name, age, gender):
    print(f" Hey {name} ! Your age is {age} and gender is {gender}")

n = input("Enter name = ")
a = int(input("Enter age = "))
g = input("Enter gender = ")

greet(n,a,g)


def discount_price(original_price, discount_percent):
    discount_amount =( discount_percent / 100 ) * original_price
    final_amount = original_price - discount_amount
    print(f" Your final amount price is Rs.{final_amount}")

discount_price(100,50)



def add(a,b):
    return a+b

ans = add(34,56)
print(ans)



# true or false return if user can vote or not
def can_vote(age):
    if age >= 18:
        return True
    else:
        return False

a = can_vote(23)
print(a)



#if prin is there in side the function if it is not returning anything if we are trying to store the result into a variable we can get none

