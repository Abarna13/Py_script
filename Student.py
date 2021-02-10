def grade(mark):
    if(mark>=90):
        return 'S'
    elif(mark>=80):
        return 'A'
    elif(mark>=70):
        return 'B'
    elif(mark>=50):
        return 'C'
    else:
        return"Fail"
roll = int(input("Enter the Roll number of the Student"))
name = input("Enter the Name of the Student")
m1 = int(input("Enter the Maths mark of the Student"))
p1 = int(input("Enter the Physics mark of the Student"))
c1 = int(input("Enter the Chemistry mark of the Student"))
total = m1+p1+c1
avg = total/3
print("\n\n\n")
print("The Roll no of the Student is",roll)
print("The Name of the Student is",name)
print("The Maths Mark of the Student",grade(m1))
print("The Physics Mark of the Student",grade(p1))
print("The Chemistry Mark of the Student",grade(c1))
print("The Total Marks of the Student",total)
print("The Average Mark of the Student",avg)