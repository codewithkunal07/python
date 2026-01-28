#set in python
# A set is a collection which is unordered, unchangeable*, and unindexed. In Python sets are written with curly brackets.
# ex.1
a = {1,2,3,4,5,6,7,8,9}
print(a)        
print(type(a))

# ex.2
b = {"apple","banana","cherry"}
print(b)

# ex.3
# we can store different data types in a set
c = {1,"kunal",3.5,True}
print(c)
# we cannot store list or dictionary in a set because they are mutable data types
# we can store tuple in a set because it is an immutable data type
d = {1,(2,3,4),5}
print(d)

# set methods
# we use this method to add an element to the set
a.add(10)
print(a)

# we use this method to remove an element from the set
a.remove(5)
print(a)

# we use clear method to remove all elements from the set
# a.clear()
# print(a)

# we use pop method to remove a random element from the set
a.pop()
print(a)

#set important methods
#union method
set1 = {1,2,3}
set2 = {4,5,6}
set3 = set1.union(set2)
print("union of set1 and set2 is :", set3)

#intersection method
set4 = {1,2,3,4,5}
set5 = {4,5,6,7,8}
set6 = set4.intersection(set5)
print("intersection of set4 and set5 is :", set6)

#lets practice 
# store following word meaning in python disctionary
a={
  "table":["a piece of furniture","list of facts and figures"],
    "cat":"a small animal"
}

print(a["table"])


#you are given a list of sunjects for students assume one classroom is required for 1 subject,how many classrooms are needed by all student
subjects = ["math","science","english","hindi","math","science","social science","english"]
print(set(subjects))
print("number of classrooms needed :", len(set(subjects)))


#wap to entr marks of 3 students from the user and store them in distionary satrt with empty dictionary's add one b one , use name subject as key's marks as value.
marks = {}
x=int(input("enter phy :"))
marks.update({"phy":x})

y=int(input("enter chem :"))
marks.update({"chem":y})

y=int(input("enter math :"))
marks.update({"math":y})

print(marks)


#figure out a way to store 9 and 9.0 as separate keys in set
#we can't do 
#s={9,9.0}
#becouse its consider as same key

#so we can use tuple to store them as separate keys
s={(9,"int"),(9.0,"float")}
print(s)

#we can also use string to store them as separate keys
s={"9_int","9.0_float"}
print(s)
