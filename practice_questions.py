# take two input and do basically all arithmatic operations
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
total = num1 + num2
print(f"The total is: {total}")
print(f"The multiplication is: {num1 * num2}")
print(f"The division is: {num1 / num2}")
print(f"The floor division is: {num1 // num2}")
print(f"The remainder is: {num1 % num2}")


#Take a number as inpput, Print Whether is is even or odd using the % operator and a comparison operator.

num = int(input("Enter a number: "))
if num % 2 == 0:
    print(f"{num} is an even number")
else:
    print(f"{num} is an odd number")

# Take the user's age as input, check and print whether they are eligible to vote (age >= 18) and whther they are senior citizen (age >= 60) print both result.

age = int(input("Enter your age = "))
can_vote = age >= 18
senior_citizen = age >= 60

print(f"User can vote: {can_vote}")
print(f"User is a senior citizent: {senior_citizen}")


#A student scored marks in 3 subjects. take all three as input calculate the total and averge

marks1 = int(input("Enter marks for subject 1: "))
marks2 = int(input("Enter marks for subject 2: "))  
marks3 = int(input("Enter marks for subject 3: "))
total_marks = marks1 + marks2 + marks3  
average_marks = total_marks / 3
print(f"Total marks: {total_marks}")
print(f"Average marks: {average_marks:.2f}")  # formatted to 2 decimal places