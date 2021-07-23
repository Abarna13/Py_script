#Python program to read positive integer and print all positive divisor of that intger.

n = int(input("Enter the Number\t"))
if(n<=0):
    print("It needs only the positive integer.")
else:
    for i in range(1,n+1):
        if(n%i==0):
            print(i,end=" ")