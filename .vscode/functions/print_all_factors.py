def print_factors():
    num  = int(input("Enter a number: "))
    for i in range(1, num + 1):
        if num % i == 0:
            print(i, end = " ")


print_factors()
# a parameter is a variable listed inside a function definition.
# an argument is the actual value you pass when calling the function
