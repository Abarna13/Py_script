x = [[12,7,3],
     [4,5,6],
     [7,8,9]]
sum = 0
for i in range(len(x)):
    for j in range(len(x[0])):
        if(i==j):
            sum = sum+x[i][j]
print("The given Matrix is")
for i in x:
    print(i)
print("The sum of diagonals is",sum)