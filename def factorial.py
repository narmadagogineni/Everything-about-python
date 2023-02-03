def factorialIterator(n):
    factorial = 1
    for i in range(n):
        factorial = factorial*(i+1)
    return factorial

# print(factorialIterator(5))     
f = factorialIterator(3)
print(f)   