def is_prime(number):
    count = 0
    for i in range(2, num +1):
        if(num % i == 0):
            count += 1
    if count == 2:
        return True
    return False
        