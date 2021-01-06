n = int(input("Enter a Number : "))
result = 0
sum = 0
while(n>0):
    result = n % 10
    sum = sum + result
    n = int(n/10)
print("The Sum of Digits of a Given Number is",sum)