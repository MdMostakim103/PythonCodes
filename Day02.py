# this is day 2:
str1 = "this is a string"
str2 = 'this is another way of creating string'
str3 = """this is another string"""  # these different type helps us to write 's 

# new line
str4 = "this is a new line following. \nthis is written in new line"
print (str4)

# string concatenation:
print (str1)
print (str2)
print (str1+str2)

# length function
print (len(str1))
print ("length of str1 :",len(str1))

# 0 base indexing just like cpp
print(str1[0])
# we can only access indexing,, that is we can't change using indexing in string


# string slicing:
print(str2[1:4])
print(str2[1:]) #this is also valid,, python does it automatically

# negative indexing: last char -1,then -2 then so on
print(str1[-3:-1])
print(str1[-1:-3:-1]) # start from -1 then stop before -3 going backwards for -1,,

# functions for string
str5="mostakim"
print (str5.endswith("m"))
print (str5.capitalize()) # this creates a temporary string with first letter capitalized
print (str5) # no changes in main string
print (str5.find("os")) #returns the starting position of substr
print (str5.count("m")) #returns the occurace of a substr

# practice:
str6=input()
print("Count of $ in your given string: ",str6.count("$"))


# conditional statement: 
# if elif else
age=int(input("give me your age: "))
if(age >= 18) : 
    print("You are an adult")
elif(age >=15) :
    print("you are a teenager")
else :
    print("welcome baby")