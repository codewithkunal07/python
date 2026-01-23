#tuple in python
# tuple is an immutable data type in python which means once we create a tuple we cannot change its values.
a= (1,2,3,4,5,6,7,8,9,)
print(a)
print(type(a))

#tuple slicing
print(a[2:5])
print(a[-7:-2]) 

#tuple methods
# we use this method to count the occurence of an element in the tuple  
print(a.count(9))
# we use this method to find the index of an element in the tuple
print(a.index(9))

#in tuple we have to write comma even for single element tuple if we don't write comma it will be considered as an integer
b = (1,)
print(type(b))


#lets practice
#wap to askk the user to enter thier 3 favorite movies and store them in a tuple
#we use this method for tuple
movie1 = input("enter your first favorite movie :")
movie2 = input("enter your second favorite movie :")
movie3 = input("enter your third favorite movie :")

favorite_movies = (movie1,movie2,movie3)
print("your favorite movies are :", favorite_movies)
print("type of favorite movies is :", type(favorite_movies))


#wap to check a list contains a palindrome of elements by copy method
list1= [1,2,1]

copylist1= list1.copy()
copylist1.reverse()
if(list1 == copylist1):
    print("list1 is palindrome")    

#wap to count the name of students with the A grade in the following tuple
students_grades = ("A","B","C","A","D","A","E","B","A")
print(students_grades.count("A"))

#store the above values in list and short them from "A" to "d"
grades = ["A","B","C","A","D","A","E","B","A"]
grades.sort()
print(grades)

#we can also convert tuple to list and sort them
grades = list(students_grades)
grades.sort()
print(grades)