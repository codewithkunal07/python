#for loops  
# for loops are used to iterate over a sequence (like a list, tuple, dictionary, set, or string)    
# PRINT THE ELIMENT OF THE FOLLOWING TUPLE USING FOR LOOP
tup = (1,4,9,16,25,36,49,64,81,100)
for element in tup:
    print(element)  

#for loos with else
tup = (1,4,9,16,25,36,49,64,81,100)
for element in tup:
    print(element) 
else:
    print("loop is ended")

#lets practice
#print the eliments of the following list using a loop (1,4,9,16,25,36,49,64,81,100)
tup = (1,4,9,16,25,36,49,64,81,100)
for element in tup:
    print(element)  

#search for a number x in tuple using loop (1,4,9,16,25,36,49,64,81,100)
tup = (1,4,9,16,25,36,49,64,81,100)
X =36
y= 0
for element in tup:
    if element == X:
        print("found",y)
        break
    y += 1


#range function
#range function is used to generate a sequence of numbers.
#syntax: range(start, stop, step)

for i in range(10):   #(start=0, stop=10, step=1)
    print(i)

for i in range(2,10):   #(start=2, stop=10, step=1)
    print(i)

for i in range(2,10,2):  #(start=2, stop=10, step=2)
    print(i)


#lets practice
#print numbers from 1 to 100
for i in range(101):
    print(i)

#print numbers from 100 to 1
for i in range(100,0,-1):
    print(i)

#print the multiplication table of n number entered by user
n = int(input("enter a number to print its multiplication table: "))
for i in range(1,11):
    print(i*n)
    
#pass statement
#pass statement is used as a placeholder for future code. when the pass statement is executed, nothing happens, but you avoid getting an error when empty code is not allowed.
for i in range(5):
    pass  # TODO: implement this later
print("loop is ended")

#lets practice
# wap to find the sum of first n natural numbers using for loop 
n = 5
sum = 0
for i in range(1,n+1):
    sum += i
print("sum is:",sum)

#wap to find the sum of first n natural numbers using while loop
n = 5
sum = 0
i = 1
while i <= n:
    sum += i
    i += 1
print("sum is:",sum)


#wap to print the factorial of a number using for loop
n = 5
factorial = 1
for i in range(1,n+1):
    factorial *= i
print("factorial is:",factorial)

#wap to print the factorial of a number using while loop
n = 5
factorial = 1
i = 1
while i <= n:
    factorial *= i
    # i += 1
print("factorial is:",factorial)
