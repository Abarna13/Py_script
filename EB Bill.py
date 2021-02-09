userid = int(input("Enter the User ID : "))
name = input("Enter the Name : ")
unit = int(input("Enter the no of units : "))
if unit == 0:
    amt = 50
elif unit<=100:
    amt = unit*1
elif unit>100 and unit<=200:
    amt = unit*2
elif unit>200:
    amt = unit*3
if amt>1000:
    surcharge = (amt*15)/100
    amt = amt+surcharge
print("The Userid is",userid)
print("The Name of the Customer is",name)
print("The Amount is",amt)