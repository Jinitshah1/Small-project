#Deleting different dictionary elements
#create a dictionary first
mydictionary = {}
mylist = list(mydictionary)
list1 = int(input("Enter the no.of elements of dictionary: "))
for n in range(0,list1):
    n = input()
    mylist.append(n)
print(mylist)
mylist.pop(3)
print(mylist)
mylist.pop(1)
print(mylist)