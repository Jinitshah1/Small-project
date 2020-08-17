#Assigning values to a list
mylist = []
list1 = int(input("Enter the no.of elements of the list: "))
for n in range(0,list1):
    n = int(input())
    mylist.append(n)
 print(mylist)
b = int(input("enter the value you want to assign to this given list: "))
mylist.append(b)
print(mylist)