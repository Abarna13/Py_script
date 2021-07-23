n = int(input("Enter the number of terms : "))
x = int(input("Enter the value of x : "))
sum = 0
for i in range(0,n):
    sum = sum+((x**i))
print("The sum of series is",round(sum,2))