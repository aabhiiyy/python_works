# ##write a program to check whether the user entered number is 2-digit/3-digit/4-digit number
# n=int(input("enter a number:"))
# if n in range(10,100):
#     print("2 digit number:")
# elif n in range(100,1000):
#     print("3 digit number:")
# elif n in range(1000,10000):
#     print("4 digit number:")
#
# ##write a basic calculator program to perform arithmetic operations (+,-,*,/,%,//)
# n1=int(input("enter first number:"))
# n2=int(input("enter second number:"))
# op=input("enter the operator")
# if op=='+':
#     print(f"sum is: {n1+n2}")
#     # print("sum is ",n1+n2)
# elif op=="-":
#     print(f"substraction is: {n1-n2}")
# elif op=='*':
#     print(f"multiplication is: {n1*n2}")
# elif op=='/':
#     print(f"division is: {n1/n2}")
# elif op=='%':
#     print(f"remainder is: {n1%n2}")
# elif op=='//':
#     print(f"{n1//n2}")
#
# ##write a program to print the number of days in a month
# m=input("enter a month:")
# l1=['january','march','may','july','august','october','december']
# l2=['april','june','september','november']
# l3=['february']
# if m in l1:
#     print("31 days")
# elif m in l2:
#     print("30 days")
# elif m in l3:
#     print("28 or 29 days")
#
# ##write a program to print the grades based on the following criteria:
# # 91-100   grade A
# # 81-90          B
# # 71-80          C
# # 61-70          D
# # below 61       E

# mrk=int(input("enter mark:"))
# if mrk>=91 and mrk<=100:
#     print("Grade A")
# elif mrk in range(81,91):
#     print("Grade B")
# elif mrk in range(71,81):
#     print("Grade C")
# elif mrk in range(61,71):
#     print("Grade D")
# elif mrk<61:
#     print("Grade E")



##write a program to check the following
#1. a no. is divisible by 2 and 3
#2. a no. is divisible by 2 and not divisible by 3
#3. a no. is divisible by 3 and not divisible by 2
#4. a no. is divisible by not 2 and 3
# n=int(input("enter a number:"))
# if n%2==0:
#     print(n,"is divisible by 2")
#     if n%3==0:
#         print(n,"is div by 3")
#     else:
#         print(n,"not div by 3")
# else:
#     print(n,"is not div by 2")
#     if n%3==0:
#         print(n,"div by 3")
#     else:
#         print(n,"not div by 3")


##write a program to check whether the entered number is
# 1.positive even or odd
# 2.negative even or odd
# n=int(input("enter a number:"))
# if n>0:
#     print("no. is positive")
#     if n%2==0:
#         print(n,"is even")
#     else:
#         print(n,"is odd")
# else:
#     print("no. is negative")
#     if n%2==0:
#         print(n,"is even")
#     else:
#         print(n,"is odd")