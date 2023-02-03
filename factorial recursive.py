#n! = 1 * 2 * 3 * 4 .....* n
#n! = 1 * 2 * 3 * 4.....(n-1) * n
#n! = n * (n-1)!

def factorialRecursive(n):
    if n ==1 or n==0:
        return 1
    return n * factorialRecursive(n-1)

f = factorialRecursive(0)
print(f)    