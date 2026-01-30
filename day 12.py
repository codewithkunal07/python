#oop in python 

#to map real world entities in programming we use oop
#oop is a programming paradigm that uses objects and classes in programming

#class and object
#class is a blueprint for creating objects
#object is an instance of a class

#example of class and object
class student:
    name = "John"
    age = 20
    grade = "A"

#creating object of class student
s1 = student()
print(s1.name)  # Output: John
print(s1.age)   # Output: 20
print(s1.grade) # Output: A


#init function
#it is a special function that is called when an object of the class is created

#constructor
#constructor is a special type of method that is called when an object is instantiated
#parameterized constructor
class student:
    def __init__(self, name, age, grade):  #init function with parameters
        self.name = name
        self.age = age
        self.grade = grade

#creating object of class student
s1 = student("Alice", 21, "B")
print(s1.name)  # Output: Alice
print(s1.age)   # Output: 21
print(s1.grade) # Output: B 

#default constructor
class student:
    def __init__(self):  #init function without parameters
        self.name = "Unknown"
        self.age = 0
        self.grade = "N/A"

#creating object of class student
s1 = student()
print(s1.name)  # Output: Unknown
print(s1.age)   # Output: 0
print(s1.grade) # Output: N/A


#class instance attributes
#why we use instance attributes
#instance attributes are used to store data that is unique to each instance of a class

#methods in class
class student:
    def __init__(self, name, age, grade):  #init function with parameters
        self.name = name
        self.age = age
        self.grade = grade

    def display_info(self):  #method to display student info
        print("Name:", self.name)
        print("Age:", self.age)
        print("Grade:", self.grade)   

#creating object of class student
s1 = student("Bob", 22, "C")
s1.display_info()  # Output: Name: Bob Age: 22 Grade: C
#creating another object of class student
s2 = student("Eve", 23, "A")
s2.display_info()  # Output: Name: Eve Age: 23 Grade: A



#static method
# static method is a method that belongs to the class rather than the instance of the class
class Math:
    @staticmethod
    def add(a, b):  #static method to add two numbers
        return a + b
result = Math.add(5, 10)
print(result)  # Output: 15



#important 
#for pillers of oop
#1.abstraction
#2.encapsulation
#3.inheritance
#4.polymorphism


#abstraction
#abstraction is the process of hiding the implementation details and showing only the functionality to the user



#lets practise
#create account class with 2 attributes_balance and account no and create a method for debit,credit and printing the balance 
  
class account:
    def __init__(self, account_no, balance):  #init function with parameters
        self.account_no = account_no
        self.balance = balance
 
    def debit(self, amount):  #method to debit amount
        self.balance -= amount
        print(rs",amount,"was" debited")
        print("current balance is:",self.balance) 
    def credit(self, amount):  #method to credit amount
        self.balance += amount
        print("rs",amount,"was credited")
        print("current balance is:",self.balance)
    
    def print_balance(self):  #method to print balance
        print("current balance is:",self.balance)

#creating object of class account
a1 = account
("123456789", 1000)
a1.credit(500)  #crediting amount