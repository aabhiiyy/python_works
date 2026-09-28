# #Write a program to check whether two entered numbers are equal or not
# n1=int(input("enter first no:"))
# n2=int(input("enter second no:"))
# if n1==n2:
#     print(n1,"and",n2,"is equal")
# else:
#     print(n1,"and",n2,"is not equal")


# #Write a program to check whether two entered words are equal or not
# w1=input("enter first word:")
# w2=input("enter second word:")
# if w1==w2:
#     print("two words are equal")
# else:
#     print("two words are not equal")


# #Write a program to find the maximum of two numbers
# n1=int(input("enter first no:"))
# n2=int(input("enter second no:"))
# # print(max(n1,n2))
# if n1>n2:
#     print("n1 is greater")
# else:
#     print("n2 is greater")


# #write a program to check whether the entered character is vowel or not
# ch=input("enter your character:")
# vo='a','e','i','o','u','A','E','I','O','U'
# if ch in vo:
#     print("vowel")
# else:
#     print("not vowel")



# #Write a program to check whether the entered country name contains word 'land'
# loc=input("enter a location:")
# if 'land' in loc:
#     print('place is',loc)
# else:
#     print('no')


# #write a program to check whether the entered number is 3 digit or not

# n1=int(input("enter a number:"))
# # if n1 in range(100,1000):
# if n1>99 and n1<=999:
#     print("n1 is a 3-digit number")
# else:
#     print("n1 is not 3-digit number")


#write a program to check whether the entered string is  palindrome or not
# s=input("enter a string")
# r=s[::-1]
# if s==r:
#     print("palindrome")
# else:
#     print("not palindrome")


#Write a program to check whether a number is present in given list
# n=int(input("enter a number:"))
# l=[23,67,12,90]
# if n in l:
#     print(n,"is present in the list")
# else:
#     print(n,"is not present in the list")


# #Write a program to check whether a key is present in a dictionary or not
# a=int(input("enter a key no:"))
# d={101:'Arun',102:'Amal',103:'Anu'}
# if a in d:
#     print(a,"is present in the dictionary")
# else:
#     print(a,"is not present in the dictionary")


# #Write a program to check whether the given password is strong/weak (if length less than 8 weak)
# password=input("enter a password")
# if len(password)<8:
#     print("password is weak")
# else:
#     print("password is strong")