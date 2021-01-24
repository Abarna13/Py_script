num = int(input("Enter the number of rows and columns"))
for i in range(num):
    for j in range(num):
        if i==0 or i==num-1 or j==0 or j==num-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
