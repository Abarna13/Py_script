import math
x = int(input("Enter the x value \t"))
n = int(input("Enter the n value \t"))
s = 0
term = x
l = 2
sign = -1
for i in range(1,n+1):
    s = s+term
    term = (sign*(x**l))/math.factorial(l)
    l = l+2
    sign = -sign
print("The sum of the sum of the series is \t",s)