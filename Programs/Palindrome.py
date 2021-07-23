n = int(input("Enter a Number : \t"))
r = 0
sum = 0
while(n>0):
    r = n%10
    sum = (sum*10)+r
    n = int(n/10)
if(n-sum):
    print("The given number is a palindrome")
else:
    print("The given number is not a palindrome")