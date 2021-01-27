def rotate(l,n):
    return l[n:] + l[:n]
list = [12,34,67,45,78,96,71]
print("List",list)
list1 = rotate(list,1)
print("Clockwise rotate by 1:",list1)
list2 = rotate(list,2)
print("Given list",list)
print("Clockwise rotate by 2",list2)
list3 = rotate(list,-2)
print("Given list",list)
print("Anti-clockwise rotate by 2:",list3)
