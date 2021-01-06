sub1 = int(input("Enter the first Subject Mark : \t"))
sub2 = int(input("Enter the second Subject Mark :\t"))
sub3 = int(input("Enter the Third Subject Mark : \t"))
sub4 = int(input("Enter the four Subject Mark :\t"))
sub5 = int(input("Enter the five Subject Mark :\t"))
def grade(mark):
    if(mark>90):
        return 'A'
    elif(mark>=80 and mark<90):
        return 'B'
    elif(mark>=70 and mark<80):
        return 'C'
    elif(mark>=60 and mark<70):
        return 'D'
    elif(mark>=50 and mark<80):
        return 'E'
    elif(mark<50):
        return 'FAIL'
print("The grade in First subject is",grade(sub1))
print("The grade in second subject is",grade(sub2))
print("The grade in Third subject is",grade(sub3))
print("The grade in Fourth subject is",grade(sub4))
print("The grade in Fifth subject is",grade(sub5))

