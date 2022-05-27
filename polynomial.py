a = int (input ("Number a : "))
x = int (input ("number x : "))

#a + ax + ax^2 + ax^3 + ..... + ax^n

n = int ( input ("Number n : "))
sum = int(0)

for i in range (n+1):
    sum += a*(x**i)

print (sum)
