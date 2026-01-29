#file I/O in python
#python can be used to perform opreations on files such as reading, writing, and appending data.

#types of file 
#1.text file
#2.binary file

# text file
#text file is a file that contains human-readable characters
#example of text file
#.txt
#.csv   

#binary file
#binary file is a file that contains data in a format that is not human-readable
#example of binary file
#.jpg
#.png
#.exe
#.pdf
#.docx


#basic opreation on files
#open,read and close file 
#we have to open a file before reading and writing 

# open("filename","mode")

f = open("name.text","r")  #open file in read mode
data =f.read()        #read file    
print(data)           #print file data
print(type(data))   #print type of data
f.close()            #close file



#diffrent type of modes
#1.read mode("r")-default mode,opens file for reading
#2.write mode("w")-opens file for writing,creates new file if file does
#3.append mode("a")-opens file for appending data to end of file
#4.read and write mode("r+")-opens file for both reading and writing
#5.binary mode("b")-opens file in binary mode
#6.text mode("t")-opens file in text mode,default mode
#7.exclusive creation mode("x")-creates new file,returns error if file already exists



# reading file
 
#data = read() -reads entire file
#data = readline() -reads single line from file

#example of readline()
f = open("name.text","r")  #open file in read mode
line1 = f.readline()        #read first line
line2 = f.readline()        #read second line
print(line1)               #print first line
print(line2)               #print second line
f.close()                  #close file

#writing to a file
f = open("name.text","w")  #open file in write mode
f.write("HELLO MY NAME IS KUNAL CHAUHAN ") #write data to file
f.close()                  #close file


#FOR APPENDING DATA TO A FILE
f = open("name.text","a")  #open file in append mode
f.write("\nI AM LEARNING PYTHON PROGRAMMING.") #append data to file
f.close()                  #close file


#EXAMPLE OF "A+" MODE
f = open("name.text","a+")  #open file in append and read mode
f.write("\nTHIS IS AN EXAMPLE OF A+ MODE.") #append data to file
f.seek(0)                  #move cursor to the beginning of the file
data = f.read()            #read file
print(data)                #print file data
f.close()                  #close file

#example of "r+" mode
f = open("name.text","r+")  #open file in read and write mode
data = f.read()            #read file
print(data)                #print file data
f.write("\nADDING NEW LINE USING R+ MODE.") #write data to file
f.close()                  #close file

#example of "w+" mode
f = open("name.text","w+")  #open file in write and read mode
f.write("\nTHIS IS AN EXAMPLE OF W+ MODE.") #write data to file
f.seek(0)                  #move cursor to the beginning of the file
data = f.read()            #read file
print(data)                #print file data
f.close()                  #close file

#WITH   STATEMENT
#it is used to open a file and automatically close it after the block of code is executed

with open("name.text","r") as f:  #open file in read mode
    data = f.read()            #read file
    print(data)                #print file data



#DELETING A FILE
import os
os.remove("name.text")  #delete file named name.text
print("File deleted successfully.")


#LETS PRACTICE
#QUESTION 1. CREATE A NEW FILE "PRACTICE.TXT" USING PYTHON ADD THE FOLLOWING DATA IN IT 
#HI EVRYONE 
#WE ARE LEARNING I/O
#USING JAVE
#I LIKE PROGRAMMING JAVE

with open("practice.txt","w") as f:  #open file in write mode
    f.write("HI EVRYONE \nWE ARE LEARNING I/O \nUSING JAVE \nI LIKE PROGRAMMING JAVE") #write data to file

#QUESTION 2. WAP THAT REPLACE ALL OCCURRENCES PYTHON WITH JAVE IN THE FILE "PRACTICE.TXT"
with open("practice.txt","r") as f:  #open file in read mode
    data = f.read()            #read file
    data = data.replace("JAVE","PYTHON") #replace JAVE with PYTHON
with open("practice.txt","w") as f:  #open file in write mode
    f.write(data)              #write data to file

#QUESTION 3. WAF TO FIND IN WHICH LINE A PARTICULAR WORD IS PRESENT IN THE FILE "PRACTICE.TXT"(USING WHILE LOOP)
# word_to_find = "PYTHON"
# with open("practice.txt","r") as f:  #open file in read mode
#     lines = f.readlines()       #read all lines
#     index = 0
#     while index < len(lines):
#         if word_to_find in lines[index]:
#             print(f"'{word_to_find}' found in line {index + 1}: {lines[index].strip()}")
#         index += 1

#FROM A FILE COUNTING NUMBERS SEPARATED BY COMMA PRINT THE COUNT OF EVEN NUMBERS
with open("numbers.txt","r") as f:  #open file in read mode
    data = f.read()            #read file
    numbers = data.split(",")  #split numbers by comma
    even_count = 0
    for num in numbers:
        if int(num) % 2 == 0:
            even_count += 1
    print("Count of even numbers:", even_count)
