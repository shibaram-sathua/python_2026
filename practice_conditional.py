#Q7  Take a number as input and print whether it is positive, negative or zero using if else statement.

num = int(input("Enter a number: "))
if num > 0:
    print(f"{num} is positive")
elif num < 0:
    print(f"{num} is negative")
else:
    print(f"{num} is zero")



# Q8 Take two numbers as input. Print the greater of the two. If they are equal, print "Both are equal".
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 > num2:
    print(f"{num1} is greater than {num2}")
elif num2 > num1:
    print(f"{num2} is greater than {num1}")
else:
    print(f"{num1} and {num2} are of same value")


#Q9 Take a leap year as input. check if it is a leap year. A year is a leap year if it is divisible by 4, but not by 100, unless it is also divisible by 400.

year = int(input("Enter the year: "))
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")