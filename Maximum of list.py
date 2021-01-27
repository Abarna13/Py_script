#Program for Maximum of a list of Numbers

n = int(input("Enter the total number of numbers in the list : "))
a = []
for i in range(0,n):
    b = int(input("Enter the Numbers : "))
    a.append(b)
print("The given list is",a)
big = a[0]
for i in range(0,len(a)):
    if(big>a[i]):
        pass
    else:
        big = a[i]
print("The Maximum of given numbers is",big)
