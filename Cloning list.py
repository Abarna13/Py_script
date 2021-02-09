print("List Cloning using Slicing : ")
a = [1,3,45,8,9,34]
b = a[:]
print(b)
print(a is b)
print("List Cloning using list() method : ")
a1 = [10,60,50,30,20]
b1 = list(a1)
print(b1)
print(a1 is b1)
a1[0] = 800
print(a1)
print(b1)
print("List Cloning using copy() method")
x = [11,12,17,18,19]
y = x.copy()
print(y)
print(x is y)