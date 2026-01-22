#list
# list is a mutable data type in python which means we can change its values.
#we can also use slicing in list
# ex.1
a = ["k","u","n","a","l"]   
print(a[2:5])

# ex.2
marks = [45,67,89,90,34 ]
marks[1:4]
print(marks) # print (marks[1:4]) to see the sliced output

# ex.3
print(marks[ :4])

# ex.4
print(marks[2: ]) #print (marks[2:len(marks)]) to see the sliced output

student = ["kunal",19,"delhi"]
print(student)
print(type(student))

print(student[0:1]) 

#string are immutable  
#list are mutable

# list can change their elements
a = ["kunal",19,"delhi"]
a[0] = "y"
print(a)


#list methods
# we use this method to add an element at the end of the list
list1 = [1,2,3,4,5]
list1.append(6)
print(list1)

#we use this method to remove an element from the list
list1.remove(3)
print(list1) 

#we use this method to remove the last element from the list
list1.pop()
print(list1)

#we use this method to add an element at a specific index
list1.insert(2,10)
print(list1)

#we use this method to sort the list
list1.sort()
print(list1)

#we use this method to sort the list in descending order
list1.sort(reverse=True)
print(list1)

#we use this method to reverse the list
list1.reverse()
print(list1)



#wap to askk the user to enter thier 3 favorite movies and store them in list
#we use this method for list

favorite_movies = []
movie1 = input("enter your first favorite movie :")
movie2 = input("enter your second favorite movie :")
movie3 = input("enter your third favorite movie :")
favorite_movies.append(movie1)
favorite_movies.append(movie2)
favorite_movies.append(movie3)
print("your favorite movies are :", favorite_movies)

#second easy method
movie = []
movie.append(input("enter your first favorite movie :"))
movie.append(input("enter your second favorite movie :"))
movie.append(input("enter your third favorite movie :"))

print( movie)