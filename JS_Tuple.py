#Accessing values from a tuple
#Tuple by ()
mytuple = ()
mylist = list(mytuple)
list1 = int(input("Enter the no.of elements you want in your list: "))
for n in range(0,list1):
    n = input()
    mylist.append(n)
print(mylist)
print(mylist[4])

