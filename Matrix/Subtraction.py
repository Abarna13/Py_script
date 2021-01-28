#Matrix Subtraction
row = int(input("Enter the number of rows : "))
col = int(input("Enter the number of columns : "))
#Matrix1
print("Enter the elements for Matrix1: ")
Matrix1 = [[int(input()) for i in range(col)] for j in range(row)]
print("Matrix1: ")
for i in range(row):
    for j in range(col):
        print(format(Matrix1[i][j],"<3"),end="")
    print()

#Matrix2
print("Enter the elements for Matrix2: ")
Matrix2 = [[int(input()) for i in range(col)] for j in range(row)]
print("Matrix2: ")
for i in range(row):
    for j in range(col):
        print(format(Matrix2[i][j],"<3"),end="")
    print()

#Result
Result = [[0 for i in range(col)] for j in range(row)]
for i in range(row):
    for j in range(col):
        Result[i][j] = Matrix1[i][j] - Matrix2[i][j]

print("The Result is : ")
for i in range(row):
    for j in range(col):
        print(format(Result[i][j],"<3"),end="")
    print()





