

def prime(n):
    if n <=1:
        return False
    if n == 2:
        return True
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

def checkprime(lst):
    return all(prime(n) for n in lst)

print(checkprime([1, 5, 3]))
