#Program for Minimum of a list of Numbers

n = int(input("Enter the total number of numbers in the list : "))
a = []
for i in range(0,n):
    b = int(input("Enter the Numbers : "))
    a.append(b)
print("The given list is",a)
small = a[0]
for i in range(0,len(a)):
    if(small<a[i]):
        pass
    else:
        small = a[i]
print("The Minimum of given numbers is",small)
