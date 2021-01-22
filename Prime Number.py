a = int(input("Enter a Number : "))
if (a == 2):
    print("The Given Number",a,"is a Prime Number")
for i in range(1,a):
    if(a%i==0):
        print("The Given Number",a,"is not a Prime Number")
        break
    else:
        print("It is a Prime Number")
