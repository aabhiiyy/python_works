# # # Q1.Define a function that takes 2 numbers and returns their product
#
# def product(n1,n2):
#     p=n1*n2
#     return p
# n1=int(input("enter a no:"))
# n2=int(input("enter a no:"))
# pr=product(n1,n2)
# print(pr)
# from functions import n2           #@@@@@@@@@@@@@@@@@@@

# # Q2.Define a function that takes a string and returns number of vowels
# #
# def vow(s):
#     c=0
#     v="aeiouAEIOU"
#     for i in s:
#         if i in v:
#             c=c+1
#     return c
# s=input("enter a string:")
# count=vow(s)
# print(count)


# # Q3.Define a function that takes length and breadth and returns area of
# #rectangle
#
# def area(l,b):
#     a=l*b
#     return a
# b=area(5,6)
# print(b)

# # Q4.Define a function that takes a list of numbers and creates a new list
# # with even numbers and returns the new list
# def list(l):
#     new=[]
#     for i in l:
#         if i%2==0:
#             new.append(i)
#     return new
# l=[45,78,90,12,35]
# print(list(l))


# #Q5.Define a function that takes list of 3 digit numbers and returns a new list where
# # each value is the sum of digits of corresponding number in the original list.
# def sum_digits(l):
#     new=[]
#     for i in l:
#         sum=0
#         for j in str(i):
#             sum=sum+int(j)
#         new.append(sum)
#     return new
# l = [123, 345, 111, 678, 134, 809]
# print(sum_digits(l))

#Q6.Define a function that takes a list and returns a new list containing unique elemnets from the given list
# def unique(l):
#     new=[]
#     for i in l:
#         if i in new:
#             continue
#         new.append(i)
#     return new
# l=[12,34,78,12,67,34,90,23]
# print(unique(l))


# #Q7.Define a function that takes 2 list as arguments and returns a new list containing common elements
# def list(list1,list2):
#     new=[]
#     for i in list1:
#         if i in list2:
#             new.append(i)
#     return new
# list1=[12,34,56,78,90]
# list2=[90,34,11,57,45]
# print(list(list1,list2))


##define a function that takes a string as argument and
# return a new dictionary where keys are words and values are length of each word call the function and print the dictionary
# {'python': 6, 'coding': 6, 'is': 2, 'easy': 4, 'and': 3, 'fun': 3}

# s="python coding is easy and fun"
# def dict(s):
#     new={}
#     for i in s.split():
#         new[i]=len(i)
#     # print(new)
#     return new
# a=dict(s)
# print(a)

##define a function that takes a number as argument and check whether that number is spy number or not
# sum of digits = product of digits
# eg: 22--> 2+2=2*2  , 1124 -->1+1+2+4=



def spy(n):
    sum=0
    p=0
    for i in str(n):
        sum=sum+int(i)
        p=p*int(i)
    if sum==p:
        print("spy number")
    else:
        print("not spy")

n=int(input("enter a number:"))
s=spy(n)
print(s)
