#recursion in python
# recursion is a process in which a function calls itself directly or indirectly
#printing numbers from 5 to 1 using recursion

def show(n):          #n is parameter
    if n>0:           #base condition
        print(n)      #print the number
        show(n-1)     #function calling itself with n-1
show(5)


#printing factorial of a number using recursion

def factorial(n):      #n is parameter
    if n == 0:        #base condition
        return 1
    else:
        return n * factorial(n-1)   #function calling itself with n-1
    
result = factorial(5)   #5 is argument
print("factorial is:",result)  # Output: factorial is: 120


#lets practice

#write a recursive function to calculate the sum of first n natural numbers
def sum_n(n):          #n is parameter
    if n == 0:        #base condition
        return 0
    else:
        return n + sum_n(n-1)   #function calling itself with n-1
    
result = sum_n(5)   #5 is argument
print("sum is:",result)  # Output: sum is: 15


#write a recursive function to print all elements of a list
def prnt_list(lst, index):   #lst and index are parameters
    if index < len(lst):   #base condition
        print(lst[index])   #print the element at current index
        prnt_list(lst, index + 1)  #function calling itself with next index

fruits = ["apple", "banana", "cherry", "date"]
prnt_list(fruits, 0)   #0 is argument for index
