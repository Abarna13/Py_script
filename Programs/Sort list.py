a = []
b = []
n1 = int(input("Enter the element for list a : "))
for i in range(1,n1+1):
    c = int(input("Enter the element : "))
    a.append(c)
n2 = int(input("Enter the element for list b : "))
for i in range(1,n2+1):
    d = int(input("Enter the element : "))
    b.append(d)
merge = a + b
merge.sort()
print("Sorted list is : ",merge)

