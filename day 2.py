#string concatenation
a = "kunal"
b="rajput"
d=" "
c= a+d+b
print(c)

#slicing
a= "kunal"
b=len(a)
print(b)

print(a[2:len(a)])
a= "kunal" 
print(a)


#negative slicing 
a= "kunal"
print(a[-5:-1])

#string methods
a="kunal rajput"
a = a.capitalize()


print(a)

#string methods
print(a.upper())
print(a.lower())
print(a.title())
print(a.replace("kunal","kumar"))


a=  "kunal"
print(a.replace("kunal","kumar"))
print (a.count("u"))


#wap to input user first and print its length
name = input("enter your name :")
print(len(name))


# wap to find the occurence of "$" in the given string
string ="$kunal$rajput$"
print(string.count("$"))


#wap to check voting eligibility

a = 12
if(a >= 18 ):
    print("eligible for voting")
else:       
    print("not eligible for voting")

#wap to input age from user and check voting eligibility
    a = input("enter your age :")
    a = int(a)  
if(a >= 18 ):
        print("eligible for voting")        
else:
        print("not eligible for voting")

#wap to check traffic light 
light = input("enter the light color :")
if (light =="green"):
      print("you can go")   
elif (light =="yellow"):
        print("get ready to stop")
elif (light =="red"):       
      print("look")
else :
    print("light is broken ")
    
#wap to input marks from user and print grade
marks = int(input("enter your marks :"))
if (marks >=90):
    print("grade A")
elif (marks >=80):
    print("grade B")        
elif (marks >=70):
    print("grade C")
elif (marks >=60):
    print("grade D")
else:
    print("fail")

    print("result of the students")

#wap to check driving eligibility
age = int(input("enter your age :"))
if (age >= 18):
    if (age >= 40):
            print("you can drive heavy vehicle")
    else:
        print("you can drive the bike")
else:
        
        print("you cant drive the bike")

#wap to check even odd
num = int(input("enter a number :"))
if (num % 2==0):
    print("even number")
else:
    print("odd number")

#wap to find the greatest of 3  number enterd by user
a = int(input("enter first number :"))
b = int(input("enter second number :"))
c = int(input("enter third number :"))
if (a>=b) and (a>=c):
    print("a is greatest")
elif (b>=a) and (b>=c):
    print("b is greatest")
else:
    print("c is greatest")

#wap to check number is multiple of 7 or not
num = int(input("enter a number :"))
if (num % 7==0):
    print("multiple of 7")
else:
    print("not multiple of 7")
