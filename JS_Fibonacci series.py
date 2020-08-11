#Fibonacci series
numbers = int(input("Enter a number: "))
#x is the initial number in the series
#y is the second number in the series
#z is the nth number in the series
x = 0
y = 1
count = 0
if numbers <= 0:
   print("Please enter a valid number")
elif numbers == 1:
   print("Fibonacci series upto",numbers,":")
   print(x)
else:
   print("Fibonacci series:")
   while count < numbers:
       print(x)
       z = x + y
       x = y
       y = z
       count += 1
