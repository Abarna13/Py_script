n = int(input("Enter the number of elements to be in the list"))
b = []
for i in range(0,n):
    a = int(input("Enter the element: "))
    b.append(a)
sum1 = 0
sum2 = 0
sum3 = 0
for j in b:
    if (j>0):
        if (j%2==0):
            sum1 = sum1 + j
        else:
            sum2 = sum2 + j
    else:
        sum3 = sum3 + j
print("Sum of all Positive Even Numbers : ",sum1)
print("Sum of all Positive Odd Numbers : ",sum2)
print("Sum of all Negative Numbers : ",sum3)
