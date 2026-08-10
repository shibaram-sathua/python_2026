# for vatriable in sequence
# this block runs for each item in the sequence

for i in range(1,6):
    print(i, end = " ")
    i = 200#there is no effect of changing the value of i
print("\n")
# steps in for loop 
for i in range(1,11,2):
    print(i, end = " ")
print("\n")
# its a negative for loop like from 10 to 1
for i in range(10,0,-2):
    #here -2 is the step here
    print(i, end = " ")

print("\n")
for i in range(1,11):
    print(i, end = " ")
print("\n")
for i in range(100, 0, -1):
    if i % 2 == 0 and i % 3 == 0:
        print(i, end = " ")

print("\n")
# dynamic for loop
start = int(input("Enter the start number"))
end = int(input("Enter the end number"))
total = 0
for i in range(start, end):
    total += i

print(total)

# break stops the loop when the condition reaches the true
# continue skip the next steps and continue from the starting part or continue the loop

sum = 0
while True:
    num = int(input("Enter a number: "))
    if num == 0:
        break
    if num < 0:
        continue
    sum += num
