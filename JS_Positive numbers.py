#Positive numbers in a range
mylist = []
totalnum = int(input("Enter total no.of elements of the list: "))
for n in range(0,totalnum):
    n = int(input())
    mylist.append(n)
    print(mylist)
list1 = mylist
olist = []
for x in list1:
    if x>=1:
        print("The positive number in the list are: ")
        olist.append(x)
        print(olist)