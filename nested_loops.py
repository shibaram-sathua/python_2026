# loop is a loop inside another loop. the inner loop completed all its iterations for every single interation of the outer loop.

# we can take a while inside a while 
# we can take a while inside a for 
# we can take a for inside for 
# usually we take a for inside a for
for i in range(1,4):
    for j in range(1,4):
        # print(f"i = {i} j = {j}")d
        print("*", end = " ")
    print("\n")

     