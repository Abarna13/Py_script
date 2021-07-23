n = int(input("Enter a Number : "))
m = int(input("Enter the number of iterations: "))
approx = (1/2) * n
for i in range(0,m):
    better = (1/2) * (approx+n/approx)
    approx = better
    print(approx)