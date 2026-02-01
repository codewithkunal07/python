#del keyword in oops
# The del keyword is used to delete objects in Python. In the context of Object-Oriented Programming (OOP), it can be used to delete attributes of a class instance or even the instance itself.  

#example

class student:
    def __init__(self,name):
        self.name = name

s1 = student("Kunal")
print(s1.name)  # Output: Kunal
del s1.name  # Deleting the name attribute

#private attributes
class student:
    def __init__(self, name, age):
        self.__name = name  # private attribute
        self.__age = age    # private attribute

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

s1 = student("Kunal", 21)
print(s1.get_name())  # Output: Kunal


#inheritance

#when a class derives from another class, it is called inheritance.
#example of inheritance
class Animal:
    def speak(self):
        return "Animal speaks"

class Dog(Animal):  # Dog class inherits from Animal class
    def bark(self):
        return "Dog barks"
    
d1 = Dog()
print(d1.speak())  # Output: Animal speaks
print(d1.bark())   # Output: Dog barks


#multi-level inheritance
class Animal:
    def speak(self):
        return "Animal speaks"
class Dog(Animal):  # Dog class inherits from Animal class
    def bark(self):
        return "Dog barks"
class Puppy(Dog):  # Puppy class inherits from Dog class
    def weep(self):
        return "Puppy weeps"
p1 = Puppy()
print(p1.speak())  # Output: Animal speaks
print(p1.bark())   # Output: Dog barks
print(p1.weep())   # Output: Puppy weeps


#multiliple inheritance
class Father:
    def skills(self):
        return "Gardening, Programming"
class Mother:
    def skills(self):
        return "Cooking, Art"
class Child(Father, Mother):  # Child class inherits from Father and Mother classes
    def skills(self):
        return Father.skills(self) + ", " + Mother.skills(self)
c1 = Child()
print(c1.skills())  # Output: Gardening, Programming, Cooking, Art


#super method
class Parent:
    def show(self):
        return "Parent show method"

class Child(Parent):
    def show(self):
        return "Child show method and " + super().show()  # calling parent class method
    
c1 = Child()
print(c1.show())  # Output: Child show method and Parent show method



#class method 
# why we use class method
# class methods are used to access or modify class state that applies across all instances of the class

class person:
    name ="anonymous"

    @classmethod
    def changename(cls,name):
        cls.name=name

p1 =  person()
p1.changename("rahul kumar")
print(p1.name)
print(person.name)



