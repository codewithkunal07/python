#loops in python
# loops are used to iterate over a sequence (like a list, tuple, dictionary, set, or string)
# WHILE LOOP
from itertools import count


i = 1
while i<=5:
    print("hello world")
    i += 1

 #print numbers from 1 tp 5
i = 1
while i<=5:
    print(i)
    i += 1

print("code is finished")

#print numbers from 5 to 1
count = 5
while count >= 1:
    print(count)
    count -= 1 

#infinite loop
# i = 1
# while i <6:
#     print(i)
#     i -=1

#lets practice
#print numbers from 1 to 100
num = 1
while num <= 100:
    print(num)
    num += 1

#print numbers from 100 to 1
num = 100
while num >= 1:
    print(num)
    num -= 1

#print the multiplication table of n number entered by user
n = int(input("enter a number to print its multiplication table: "))
i = 1
while i <= 10:
    print(i*n)
    i += 1

#PRINT THE ELIMENT OF THE FOLLOWING LIST USING WHILE LOOP
# [1,4,9,16,25,36,49,64,81,100]

lst = [1,4,9,16,25,36,49,64,81,100]
i = 0
while i < len(lst):
    print(lst[i])
    i += 1

#SEARCH FOR A NUMBER X IN TUPLE USING LOOP (1,4,9,16,25,36,49,64,81,100)
tup = (1,4,9,16,25,36,49,64,81,100)
X =36
i = 0
while i < len(tup):
    if tup[i] == X:
        
        print("number found",i)
        break
    else:
        print("finding.....")
    i += 1
print("end of loop")


#break statement
i = 1
while i <= 10:
    print(i)
    if i == 5:
        break
    i += 1  

print("loop ended")

#continue statement
i = 0
while i <= 5:
    if (i == 3):
        i += 1
        continue
    print(i)
    i += 1
    print("loop ended")
    
#wap to print even numbers from 1 to 10 using continue statement
i = 1
while i <= 10:
    if (i % 2 == 0):
        i += 1
        continue
    print(i)
    i += 1