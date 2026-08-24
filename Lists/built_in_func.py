# len()
# min()
# max()
# sum()
# sroted()
# it eill count the lenth from 1 
marks  = [447,3984,948,87,89,44,90]
print(len(marks))
# retunrs the smallest item from a list of numbers
print(min(marks))
# return the largest item from a list of numbrs
print(max(marks))
# returns the sum of the numeric elements in the list
print(sum(marks))
#returns a new list containing all items from the iterable in ascending order. The original list remains underchanged
print(sorted(marks))
print(sorted(marks, reverse = True))

# print(sorted(marks), reverse = False)# there is no method like this

print(marks)


#practical use  calculating average marks
average = sum(marks) / len(marks)
print(f"Average : {average: .2f}")# output: Average : 85.00