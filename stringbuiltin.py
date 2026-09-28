# # Write a program to create a list of 5 random 3 digit numbers
# import random
# new=[]
# for i in range(5):
#     new.append(random.randint(100,1000))
# print(new)
#
#
# #write a program to create a 5 digit random otp number
import random
print(random.randint(10000,100000))
#
#
# #write a program to find the position of a character in a string
# s="hello"
# print(s.index('l'))

#
#
# #define a function that takes a string as argument and returns a new dictionary
# #where keys are character and values are count of each character
#
# s="pythonn"
# def arg(s):
#     new={}
#     for i in s:
#         new[i]=s.count(i)
#     print(new)

# arg('singdsss')
#
#
# #Define a function that takes string as argument and print the count of digits,spaces,letters in that string
#
def dsl(s):
    d=0
    sp=0
    l=0
    for i in s:
        if  i.isdigit():
            d=d+1
        elif i.isspace():
            sp=sp+1
        elif i.isalpha():
            l+=1
    print("digits =",d,' spaces =',sp,' letters =',l)
dsl(' hello 1 23 ')