x = int(input("Enter the x value \t"))
n = int(input("Enter the n value \t"))
s = 0
term = x
l = 1
for i in range(1,n+1):
    s = s + term
    term = (term*x*x*x*(-1))/((l+1)*(l+2))
    l = l + 2
print("The sum of the sum of the series is \t",s)