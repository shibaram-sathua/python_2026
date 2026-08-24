# A lambda function is a small anonymous function written in a single line. It is a useful when you need a simple function for a short  period and do not want to family it with def.
#normal function 
def square(n):
    return n * n

#same thing as a lambda
s = lambda n: n ** 2
print(s(5)) #25



def add(a, b):
    print( a + b )

#same thing as lambda
add = lambda  a, b: a+b
print(add(3,4))



#return True if age>= 18 else false
def is_adult(age):
    if age >= 18:
        return True
    return False

is_Adult = lambda age: True if age >= 18 else False
print(is_Adult(23))