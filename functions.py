# # without using function , normal code
#
# n1=int(input("enter a no:"))
# n2=int(input("enter a no:"))
# s=n1+n2
# print("sum",s)

# # using function

# def add():
#     "addition of 2 numbers"
#
#     n1=int(input("enter a no:"))
#     n2=int(input("enter a no:"))
#     s=n1+n2
#     print("sum:",s)
#
#     return            #it is not needed bcz this prgrm exit when it is done
# add()


# #define a function to display "hello your name"
#
# def name():
#     n=input("enter your name:")
#     print("hello",n)
#     return
# name()


# # define a function to find the factorial of a number
#
# def factorial():
#     n=int(input("enter a no:"))
#     f=1
#     for i in range(1,n+1):
#         f=f*i
#     print("factorial",f)
#     return
# factorial()


# # define a function to find the count of a specific character in a given string
#
# def count():
#     s=input("enter a string:")
#     ch=input("enter a character:")
#     c=0
#     for i in s:
#         if i==ch:
#             c=c+1
#     print("count",c)
#     return
# count()


# # define a function to check whether a number is prime or not
#
# def check_prime():
#     n=int(input("enter no:"))
#     if n>1:
#         for i in range(2,n):
#             if n%i==0:
#                 print("not prime")
#                 break
#         else:
#             print("prime")
#     else:
#         print("number is neither prime nor composite")
#     return
# check_prime()
#
# # # define a function to find the factors of a number
# def factors():
    # n=int(input("enter a number:"))
    # for i in range(1,n+1):
    #     if n%i==0:
    #         print(i)
    # return
# factors()
# factors(int(input("enter a number:")))

# def add(n1,n2):
#     s=n1+n2
#     print("sum",s)
#     return
# add(23,45)
#
# ##dynamic
# def add(n1,n2):
#     s=n1+n2
#     print("sum",s)
#     return
#
# a=int(input("enter a no:"))
# b=int(input("enter a no:"))
# add(a,b)

# # define a function that takes amount,year and rate as arguments and find the simple interest value.(dynamic input)
# # si=p*n*r/100
#
# def simple_interest(p,n,r):
#     si=p*n*r/100
#     print(si)
#     return
#
# p=int(input("price:"))
# n=int(input("no. of year:"))
# r=int(input("rate:"))
# simple_interest(p, n, r)

## define a function that takes 2 numbers as arguments and result sum as result call the function and print the result
# def sum(n1,n2):
#     sum=n1+n2
#     return sum
# a=sum(30,21)
# print(a)


# def sum(n1,n2):
#     sum=n1+n2
#     return sum
# n1=int(input("enter a no:"))
# n2=int(input("enter a no:"))
# a=sum(n1,n2)
# print(a)


# def arm(n):
#     s=str(n)
#     l=len(s)
#     sum=0
#     for i in s:
#         sum=sum+int(i)**l
#     if sum==n:
#         # print("armstrg")
#         return "armstrg"
#     else:
#         # print("not armdtrg")
#         return "not armstrg"
# n = int(input("no:"))
# r=arm(n)
# print(r)

def maxi(lr,n):
    lr=n[0]
    for i in n:
        i>lr
        lr=i
    return lr
print(max(1,5,6,368,8,3,55))