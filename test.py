'''
print("Hello this is 'Saikat'" )

print("these are mountain /\\/\\")# how to print escape sequence

print("hello \\t Roy")#use of escape sequence




j=3

#j++ type increment not supported in Python

#print(j++) is an error in python
print(j+1)

print(j)
'''

'''
#by default variables store in string format while using input()
name= input("what's your name ? ")

age = int(input("How older you ? "))

#Way-1 of printing
print("{var1} you are {var2} year's old".format(var1=name,var2=age))

#Way-2 of printing
#This type printing introduce in Python 3.6 
print(f"{name} you are {age} year's old")
'''

'''
#Declaring multiple variable in same line

name , age = "Saikat",24 #valid and we have to maintain the sequence of declaration and initialization.

print(f"{name} is {age} year's old")
'''

'''
#taking multiple input in one line ->

name , age = input("Enter your name and age [separated by space]").split()

print(f"{name} is {age} year's old")


name1 , age1 = input("Enter your name and age [separated by 'comma']").split(",") 

print(f"{name1} is {age1} year's old")
'''
'''
#calculating avarage

num1,num2,num3=input("Enter 3 number followed by comma ").split(",")

print(f"Avarage of {int(num1)} ,{int(num2)}, {int(num3)} is : {(int(num1)+int(num1)+int(num1))/3}")
'''

#Reversing a String in simplest way possible;)
'''
myString="Computer Science and Engineering"

reverseString = myString[::-1] 

print(reverseString)
'''

'''
#finding how many times a particular charecter repeated

name_string , char_input = input("Input a String and character you want to find in that string [separated by comma] :").split(",")


print(f"Input string length : {len(name_string)}")

print(f"{char_input} repeated {name_string.upper().count(char_input.upper())} times")

#use of strip method

name = "    Saikat     "
testString='+++++++++'

print(name+testString)

print(testString+name.rstrip()+testString) #rstrip() method remove all spaces from right side of the string

print(testString+name.lstrip()+testString) #lstrip() method remove all spaces from left side of the string

print(testString+name.strip()+testString) #strip() method remove all spaces from both side of the string.

name="Saik    at"
print(name.strip()) #Strip method can't remove spaces from middle of any string for that we use replace method

#Use of Find and Replace Method :

#replace():

testStr = "There is three cow. who is Maa Kali ? , is she Divine Mother ?"

print(testStr.replace("is", "was",2)) #replace("PRESENT_WORD", "WORD_WANTED_TO_REPLACE",HOW MANY WORD WANT TO REPLACE)

#find():

print(testStr.find("is")) #returns the index position of the char in the string

is_pos1=testStr.find("is")
print(testStr.find("is",is_pos1+1)) #returns the index position of the char after the mentioned index position


'''

#use of else if and elif ->


'''
age = int(input("Enter your Age ? "))

if age >= 18 :
    print("You Can Enter Here")

else :
    print("You can't Enter")
'''

#IF you are over 18 and your name starts with 'A' or 'a' then only you can play
'''
name = input("Enter your name : ")

age = int(input("Enter your age : "))

if name[0].upper()=='A' and age >=18 :
    print("You can Play")
else:
    print("Sorry!!!! you can't play")

'''
'''
# in keyword with if :

name = "Saikat"

if("z" in name): #it simply searching for z in the given string if found then it return true otherwise false
    print("You are Lucky")
else:
    print("Better luck next time")

'''

'''
# printing first n numbers sum using while loop

numberN = int(input("any natural number : "))

i=1
sum=0
while(i<=numberN):
    sum=sum+i
    i=i+1
print(f"Sum is {sum}")
'''

'''
#taking input of a number and adding every digit

input_number_string = input("Enter your desire number : ")
total_number=0

i=0
while(i < len(input_number_string)):
    total_number= total_number + int(input_number_string[i])
    i=i+1

print(f"Sum of {input_number_string} is {total_number}")
'''
'''
#counting how many times a charecter is repeated in a String
name_string = input("Enter Your name : ").upper()

i=0
while(i < len(name_string)):
    print(f"{name_string[i]} is repeated {name_string.count(name_string[i])} times")
    i=i+1


#for loop example:

for i in range(10):
    print(f"i value : {i}")

#for loop example with mentioned range:

print("\n-------------------\n")

for i in range(2,21): #i value starts from 2 and go till 21
    print(f"i value : {i}")

'''

#counting repeated char in a given String :
'''
name_string = input("Enter your name : ").upper()

temp=""

for i in range(0,len(name_string)):
    
    if (name_string[i] not in temp): #checking if the particular char is there on temp variable
        print(f"In {name_string} '{name_string[i]}' char repeated {int(name_string.count(name_string[i]))} times")
    
    temp+=name_string[i] # Adding every char after counting to stop printing multiple times

print("Counting Completed ;)")

'''


#printing even number with typical math :
'''
print("Even numbers : \n")

for i in range(2,20):
    
    if(i/2):
        print(i)

print("\n")
###############################
        
#Shortest way :
print("Even numbers : \n")
for i in range(2,4002,2):
    print(i)
    
#reverse printing using for
'''
'''

for i in range(11,0,-1): #mandatory to mention the steps otherwise nothing will print
    print(i)


while True:
    print('G')


'''

# let's define a function that will return a last char of a input String
# in python always define function before use

'''
def return_last_char(name):
    return name[-1]

name = input("Enter a String : ")
print(f"Last char of {name} is : {return_last_char(name)}")
'''
'''
def which_num_bigger(num1,num2):
    if(num1>num2):
        return num1
    return num2

num1,num2 = input("Enter two number:  ").split(",")

print(which_num_bigger(int(num1),int(num2)))
'''

#finding bigger number using function inside funtion call ->
'''
def greater(num1,num2):
    if(num1>num2):
        return num1
    return num2

def bigger_num_using_recursion(num1,num2,num3):
    return greater(greater(num1,num2),num3)

print(bigger_num_using_recursion(23,60,56))
'''

#checking a string if that one is palindrome or not :
'''
def if_palindrome(check_string):
    return check_string.upper() == check_string[::-1].upper()




check_string_bool = if_palindrome(input("Input a String : "))

if(check_string_bool==True):
    print("Yes Palindrome;)")
    
else:
    print("Not it is not :(")

'''
#printing fibonichi series of a given range

'''
def fibbonici_num(num2):
    i=0
    j=1
    m=0
    print(i)
    for k in range(0,num2): #k=1 , k<num2
        print(i+j,end=" ")
        m=i+j
        j=i
        i=m
    
    return   
        
        
num1 = int(input("Enter a number : "))
fibbonici_num(num1)
'''

#in case of python we can provide default value while function declaration : my_func(a,b=4,c=56)
#advantage : if you don't provide any argument (but it is necessary to provide value of 'a' , as 'a' doesn't have default value) while func call then the default value will be use.
#if value is provided while func call then default value will be replace with provided value.
#NOTE : default value while func declaration will be always at end :

#   math_func(b=4,a) ----> will throw an error
#   math_func(k,b=4,a) ----> will throw an error
#   math_func(a,k,b=4,c=34,d="Swami Vivekananda") ----> is OK.
'''
def math_func(a,b=4):
    print(a+b)

math_func(23,5)
'''

#exception_handling
#work like Java ->
'''
try:
    a=10
    b=0
    c=a/b

except ZeroDivisionError :
    print("Here is an error !!!!!!")
finally:
    print("Finally Block Executed")

'''

#working with file :

#>>>Opening a file:

'''
#meth-1:

file1 = open("test.txt","r") #open(FILE_NAME , MODE_OF_OPEN{READ or WRITE or APPEND or both READ+WRITE})

file1.close()

#meth-2:

with open("test.txt",r) as file2 :
    #here we will put statement.
'''


#>>>Reading from a file:

#meth-1:

file1 = open("test.txt","r") #open(FILE_NAME , MODE_OF_OPEN{READ or WRITE or APPEND or both READ+WRITE})

'''
reading_file = file1.read()
print(reading_file)
'''

#we can specify how many charecter we want :

'''
reading_file = file1.read(5)
print(reading_file)
'''
#we can print only one line :
'''
reading_file = file1.readline()
print(reading_file)
'''

#we can print all lines in the form of list :
'''
reading_file = file1.readlines()
print(reading_file)
file1.close()
'''
#meth-2:

with open("test.txt","r") as file2 :
   reading_file = file1.read()
   print(reading_file) 

#no need to close the file in this method.












