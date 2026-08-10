# print all the numbers which are divisible by 3 and 5 from 1 to 100
start = 1
end = 100
i = start
while i <= end:
    if i % 3 == 0 and i % 5 == 0:
        print(i, end = " ")
    i += 1

print("\n")
#sum of all numbers from 1 to 100
sum = 0
start = int(input("Enter the start number: "))
end = int(input("Enter the end number: "))
while start <= end:
    sum = sum + start
    start += 1

print(f"{sum}")

# ask a number from the user, and print all the factors
print("\n")

user_input = int(input("Enter num: "))
i = 1
# count = 0
while i <= user_input/2:
    if user_input % i == 0:
        print(f"{i}", end = " ")
        # count = count + 1
    i += 1

print(f"{user_input}")
# print(count)