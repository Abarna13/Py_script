num = int(input("Enter the Number of Terms : "))
f1 = 0
f2 = 1
f3 = f1 + f2
print("Fibonnacci series of First",num,"Terms : ")
print(f1)
print(f2)
for i in range(3,num+1):
    print(f3)
    f1 = f2
    f2 = f3
    f3 = f1 + f2