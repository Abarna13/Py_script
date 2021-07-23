#Searching an element in a list using linear search Technique

list = [1,78,3,56,6,7,98]
search = int(input("enter the search element : "))
for i in range(0,len(list)):
    if search == list[i]:
        print(str(search)+(" Found at Position ")+str(i))
