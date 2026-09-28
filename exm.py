# --------------------------1. function-------------------------

# # 1. Define a function that accepts two lists and returns the elements that are common to both lists without using set().
# def cm():
#     new=[]
#     l1=[1,2,3,4,5,7]
#     l2=[2,4,53,5,12,79]
#     for i in l1:
#         if i in l2:
#             new.append(i)
#     return new
# print(cm())
#
# # 2. Define a function that takes a number as an argument and returns True if the number is divisible by the sum of its digits.
# # Example: 18 → 1 + 8 = 9, and 18 % 9 = 0.
#
# def sd(n):
#     sum=0
#     for i in str(n):
#         sum=sum+int(i)
#     if n%sum==0:
#         return "true"
#     else:
#         return "false"
# print(sd(18))

# # 3. Define a function that takes a list containing numbers from 1 to n with 1 no. is missing and returns the missing no.
# # eg: [1,2,3,5,6] --> 4
# def ms():
#     l=[1,2,3,5,6]
#     for i in range(1,7):
#         if i in l:
#             continue
#         else:
#             print(i)
# ms()

# # 4. Define a function that takes a number as an argument and prints its multiplication table from 1 to 10. Call the function.
# def mul(n):
#     p=1
#     for i in range(1,11):
#         # p=n*i
#         print(n,'x',i,'=',n*i)
#     return
# mul(13)

#         -----or------

# def mis(n):
#     i=1
#     p=1
#     while i<=10:
#         p=n*i
#         print(n,'x',i,'=',p)
#         i=i+1
#     return
# mis(5)


# # 5. Prime numbers upto a given number
#
# def fun(n):
#     new = []
#     for i in range(3, n):
#         for j in range(2, i):
#             if i % j == 0:
#                 break
#         else:
#             new.append(i)
#     return new
# h = fun(20)
# print(h)


# ------------------------------------2. python core--------------------------------------

# # 1. Print Series
#
# # a.1 8 27 64 125
#
# for i in range(1,6):
#     print(i**3,end=" ")
# print()

# # b.100 90 80 70 60 50
#
# for i in range(100,40,-10):
#     print(i,end=" ")
# print()
#
#      # ----or----
#
# for i in range(10,4,-1):
#     print(i*10,end=" ")
# print()

# # c.1 3 6 10 15 21
#
# a=1
# for i in range(2,8):
#     print(a, end=" ")
#     a=a+i
# print()

# # d.1 10 100 1000 10000
#
# c=1
# for i in range(1,6):
#     print(c,end=" ")
#     c=c*10
# print()

# # e.3 6 9 12 15 18
#
# for i in range(1,7):
#     print(i*3,end=" ")
# print()

# # 2.Given a list L=[0,1,0,3,12]
# #  Write a program to Move all  zeroes to the end
# #  output:[1,3,12,0,0]
#
# L=[0,1,0,3,12]
# for i in L:
#     if i==0:
#         L.remove(i)
#         L.append(0)
# print(L)


# # 3.Write a program to find the Count of vowels and consonants in a string
# # string="Python is a programming language"
#
# string = "Python is a programming language"
# vowels = "aeiouAEIOU"
# v_count = 0
# c_count = 0
# for ch in string:
#     if ch.isalpha():   # only consider letters
#         if ch in vowels:
#             v_count += 1
#         else:
#             c_count += 1
#
# print("Vowels:", v_count)
# print("Consonants:", c_count)


# # 4.Define a function that takes a list as argument and returns the Most frequent number in a list.
# # Eg:l=[1,2,2,3,4,2,5,3,4,6]
# # Output:2
#
# def most_frequent(l):
#     max=0
#     ans=0
#     for i in l:
#         c=l.count(i)
#         if c>max:
#             max=c
#             ans=i
#     return ans
# print(most_frequent([1, 2, 2, 3, 4, 2, 5, 3, 4, 6]))


# # 5.Print Pattern
# # 1 1 1 1 1
# # 2 2 2 2
# # 3 3 3
# # 4 4
# # 5
#
# for i in range(1,6):          # numbers from 1 to 5
#     for j in range(6-i):     # decreasing count each row
#         print(i, end=" ")
#     print()
