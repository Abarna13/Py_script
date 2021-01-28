#Matrix Multiplication
p = int(input("Enter the row number for matrix1 : "))
q = int(input("Enter the col number for matrix2 : "))
n = int(input("Enter the col number for matrix1 / row number of matrix2: "))
#Matrix1
print("Enter the elements for Matrix1: ")
Matrix1 = [[int(input()) for i in range(n)] for j in range(p)]
print("Matrix1: ")
for i in range(p):
    for j in range(n):
        print(format(Matrix1[i][j],"<5"),end="")
    print()

#Matrix2
print("Enter the elements for Matrix2: ")
Matrix2 = [[int(input()) for i in range(q)] for j in range(n)]
print("Matrix2: ")
for i in range(n):
    for j in range(q):
        print(format(Matrix2[i][j],"<3"),end="")
    print()

#Result
Result = [[0 for i in range(q)] for j in range(p)]
for i in range(p):
    for j in range(q):
                for k in range(n):
                    Result[i][j] = Result[i][j] + Matrix1[i][k] * Matrix2[k][j]

print("The Result is : ")
for i in range(p):
    for j in range(q):
        print(format(Result[i][j],"<5"),end="")
    print()





