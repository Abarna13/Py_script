lst = []
num = int(input("Enter the number of elements in a list \t"))
for n in range(num):
    numbers = int(input("Enter the number \t"))
    lst.append(numbers)

found = False

x = int(input("Enter the number to be searched \t"))
for i in range(len(lst)):
    if x == lst[i]:
        found = True
        print("\n%d found at position %d" % (x,i))
        break
if not found:
    print("\n%d  is not found in the list" % x)

