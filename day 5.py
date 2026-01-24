#dictionary 
# A dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets, and they have keys and values.

# ex.1
a = {"name":"kunal","age":19,"city":"delhi"}
print(a)
print(type(a))

# ex.2
b = {1:"apple",2:"banana",3:"cherry"}
print(b)

# ex.3
#we can store list and tuple as values in dictionary and keys must string or integer

c = {"name": "kunal",
       "subject": ["sql","python","power bi"],
       "tpic": ("data analysis","data visualization")
}
print(c)
print(c["subject"]) 

#modifying value in dictionary 
c["subject"] = ["html","css","javascript"]
print(c)

#adding new key value pair in dictionary
c["surname"] = "rajput"

#null dictionary
d = {}
print(d)
print(type(d))

#nesting dictionary
student1 = {
    "name": "kunal",
    "age": 19,
    "marks": {
        "maths": 95,
        "science": 90
    }
}
print(student1)
print(student1["marks"]["maths"]) 


#disctionary methods
# we use this method to get all the keys of the dictionary
print(student1.keys())
# we use this method to get all the values of the dictionary
print(student1.values())
# we use this method to get all the items of the dictionary 
print(student1.items())
# we use this method to get key value pair using get method
#we use get method instead of square brackets to avoid error if key is not present in dictionary
print(student1.get("name"))
# we use this method to update the dictionary
student1.update({"age":20})
print(student1)
