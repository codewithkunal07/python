#function in python
#function is a block of code which only runs when it is called
def greet():
    print("Hello, welcome to the world of Python functions!")
greet()  # Calling the function to execute its code         

#calculate the sum of two numbers using function
def add_numbers(a, b):
    sum = (a+b)
    return (sum)

print(add_numbers(5, 10) )  # Output: 15
 

 #we can also write the function to return a value
def multiply_numbers(x, y):
    return x * y 
result = multiply_numbers(4, 5) # Storing the returned value in a variable
print(result)  # Output: 20

#without parameter function
def say_hello():
   print("Hello!")
output = say_hello()  # Output: Hello!
print(output)  # Output: None


#avg of three numbers using function
def average_of_three(num1, num2, num3):
    sum =(num1+num2+num3)
    avg = sum / 3
    print(avg)  
    return avg
    

average_of_three(12, 20, 42)


#using if in function 
def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
result = check_even_odd(7)
print(result)  # Output: Odd


#function using loop
def print_numbers(n):
    for i in range(1, n + 1):
        print(i)

print_numbers(5)  # Output: 1 2 3 4 5   


#printing multiple values on same line
print("Hello", end=" ")
print("World!")  # Output: Hello World!


#function python 
#there is two types of function
#1.builtin function
#2.user defined function

#builtin function
#example of builtin function
#those function which is pre defined in python is called builtin function
numbers = [5, 2, 9, 1]
sorted_numbers = sorted(numbers)
print(sorted_numbers)  # Output: [1, 2, 5, 9
print(len(sorted_numbers))  # Output: 4
print(max(sorted_numbers))  # Output: 9
print(min(sorted_numbers))  # Output: 1
print(sum(sorted_numbers))  # Output: 17
print(type(sorted_numbers))  # Output: <class 'list'>
print(range(5))  # Output: range(0, 5)
print(abs(-10))  # Output: 10
print(round(3.6))  # Output: 4


#user defined function
#those function which is defined by user is called user defined function
def square(number):
    return number * number
result = square(6)
print(result)  # Output: 36



#default parameter function
def cal(b,a=2):
    print(a*b)
    return(a*b)


cal(1)



#waf to print the length of the list
cities =["delhi","gurgaon","noida","faridabad"]
heroes =["thor","iron man", "caption america"]


def print_length(lst):
    length = len(lst)
    return length

print(print_length(cities))



#waf to print the element of a list in a singal line (list is the parameter)
def print_list(list):
    for i in list:
     print(i, end=" ")
    
print_list(heroes)


#waf to find the factorial of n (n is the paramenter)
 
def factorial(n):
     facto = 1
     for i in range(1,n+1):
         facto *= i
     print(facto)

factorial(2)


#waf to convert usd to inr
def usd_to_inr(usd):
    inr = usd * 82.74  # Assuming 1 USD = 82.74 INR
    return inr
amount_in_inr = usd_to_inr(100)
print(amount_in_inr)  # Output: 8274.0


# waf to take a number as input and return string"even" if the number is even and "odd" if the number is odd
def check_even_odd(number):
    if number % 2 == 0:
        return "even"
    else:
        return "odd"

result = check_even_odd(7)
print(result)  # Output: odd