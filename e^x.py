# e^x = 1 + x + x^2/2! + x^3/3! + x^4/4! + ...
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def e(x):
    sum = 1
    for i in range(1, 997):
        sum += (x ** i) / factorial(i)
    return sum

print(e(10))