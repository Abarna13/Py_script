a = []
c = []
n1 = int(input("Enter number of elements : "))
for i in range(1,n1+1):
    b = int(input("Enter elements:"))
    a.append(b)
n2 = int(input("Enter number of elements : "))
for i in range(1,n2+1):
    d = int(input("Enter elements:"))
    c.append(d)
new = a+c
print("Merged list is : ",new)
