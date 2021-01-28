#Another Method for Matrix Multiplication

x = [[13,5,6],
     [7,9,65],
     [8,14,16]]
y = [[5,8,1,2],
    [6,7,3,0],
    [4,5,9,1]]
result =[[0,0,0,0],
        [0,0,0,0],
        [0,0,0,0]]
for i in range(len(x)):
    for j in range(len(y[0])):
        for k in range(len(y)):
            result[i][j] += x[i][k] * y[k][j]
print("The Result of the Matrix Multiplication is : ")
for r in result:
    print(r)