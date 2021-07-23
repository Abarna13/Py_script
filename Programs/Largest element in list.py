n = int(input("Enter the total number of numbers in the list"))
a = []
for i in range(0,n):
    b = int(input("Enter the numbers : "))
    a.append(b)
print("The given list is",a)
a.sort()
print("Sorted list",a)
print("First largest element in list",a[n-1])
print("Second largest element in list",a[n-2])
print("Third largest element in list",a[n-3])