rows = int(input("Enter the row value : "))
space = rows - 1
for i in range(0, rows):
    for j in range(0, space):
        print(" ", end = "")
    for j in range(0, i+1):
        print("* ", end = " ")
        space = space - 1
    print()

