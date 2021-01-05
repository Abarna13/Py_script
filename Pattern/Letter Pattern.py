rows = int(input("Enter the row value : "))
Ascii = 65
for i in range(0, rows):
    for j in range(0, i+1):
        value = chr(Ascii)
        print(value, end = " ")
    Ascii += 1
    print()