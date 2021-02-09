print("List Aliasing : ")
a = [6,8,9,67,45]
b = a
print(b)
print(a is b)
a[0] = 876
print(a)
print(b)