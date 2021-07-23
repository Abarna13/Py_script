s = input("Enter a String : ")
c = 0
for i in s:
    if i in "aeiouAEIOU":
        c = c + 1
print("The Number of Vowels in",s,"is",c)