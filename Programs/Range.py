#To check whether the given number is in range or not

def testrange(a,b,n):
    if n in range(a,b):
        print("Inside the given Range")
    else:
        print("Outside the given Range")
a = int(input("Enter  the Lower Limit:"))
b = int(input("Enter  the Upper Limit:"))
n = int(input("Enter  the Number:"))
testrange(a,b,n)