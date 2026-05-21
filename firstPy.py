print("hi i am learning python","what is happeneing. ",23+45)
print("i am what i am")
name="mostakim"
age=23
price=34.44
print(age,price,name)
print(type(price))

print("for comment we use # for one line comment")
#what's app? hehe
print("i have already commented a line")

#divide will give me floating value unlike cpp or c;
#arithmetic operators are same as cpp
#extra operator : power operator--> a**b == a^b

#relational operator is same as cpp

#assignment operator is same as cpp,,, except: a**=b means 
#a will be equal to current value of a**b;

#logical operators
# not(!) , or(||) , and(&&)
# expr1 and expr2  ==== expr1 && expr2

# type conversion: 1.type conversion-auto 
#                  2.type casting-explicit

a=3
b=3.244
sum=a+b  # sum becomes float by implicit conversion

c="2"
d=2.34
# sum2=c+d  ,, this will create error
sum2=int(c)+d
print("sum: ",sum)
print("sum2: ",sum2)