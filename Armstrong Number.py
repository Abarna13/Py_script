num = int(input("Enter the Number : "))
sum = 0
temp = num
while temp > 0:
    digit = temp % 10
    sum = sum +(digit ** 3)
    temp = temp / 10
if num == sum:
    print(num,"is an Armstrong Number")
else:
    print(num,"is not an Armstrong Number")

