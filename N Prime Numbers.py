# Python Program to find N Prime Numbers
max = int(input(" Please Enter Any Number: "))
Number = 1
print("Prime numbers between", 1, "and", max, "are:")
while(Number <= max):
    count = 0
    i = 2

    while(i <= Number//2):
        if(Number % i == 0):
            count = count + 1
            break
        i = i + 1

    if (count == 0 and Number != 1):
        print(" %d" %Number, end = '  ')
    Number = Number  + 1

