import math

def isPrime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    else:
        for i in range(math.sqrt(n)):
            if i % n:
                return False

    return True