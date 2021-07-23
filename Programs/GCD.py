num1 = int(input("Enter the first Number : "))
num2 = int(input("Enter the second Number : "))
for i in range(1,min(num1,num2)+1):
    if (num1%i==0 and num2%i==0):
        gcd=i
print("Gcd of",num1,"and",num2,"is : ",gcd)