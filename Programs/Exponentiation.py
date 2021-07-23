n = int(input("Enter a number : "))
e = int(input("Enter the exponent : "))
r = n
for i in range(1,e):
    r = n * r
print("The value is : ",r)