# ## 1. Basics (Input & Output)
#
# # 1. Print `"Hello, World!"`.
# print("Hello, World!")
#
# # 2. Read a person's name and print a greeting.
# name=input("Enter your name:")
# print("hi",name+',',"it's good to see you")
#
# # 3. Read two numbers and print their sum.
# n1=int(input("enter first no:"))
# n2=int(input("enter second no:"))
# sum=n1+n2
# print("sum=",sum)
#
# # 4. Find the area of a rectangle.
# b=int(input("enter breadth:"))
# h=int(input("enter height:"))
# area=b*h
# print("area=",area)
#
# # 5. Convert Celsius to Fahrenheit.
# c=float(input("enter celsius:"))
# f=(c*9/5)+32
# print("fahrenheit=",f)
#
# ---
#
# ## 2. If-Else
#
# # 6. Check whether a number is positive, negative, or zero.
# n=int(input("enter a no:"))
# if n>0:
#     print("postive number")
# elif n<0:
#     print("negative number")
# else:
#     print("number is zero")
#
# # 7. Check whether a number is even or odd.
# n=int(input("enter a no:"))
# if n%2==0:
#     print("even number")
# else:
#     print("odd number")
#
# # 8. Find the largest of two numbers.
# n1=int(input("enter first no:"))
# n2=int(input("enter second no:"))
# if n1>n2:
#     print(n1,"is greater than",n2)
# else:
#     print(n2,"is greater than",n1)
#
# # 9. Find the largest of three numbers.
# n1=int(input("enter first no:"))
# n2=int(input("enter second no:"))
# n3=int(input("enter third no:"))
# if n1>n2 and n1>n3:
#     print(n1,"is greater than",n2,"and",n3)
# elif n2>n1 and n2>n3:
#     print(n2,"is greater than",n1,"and",n3)
# else:
#     print(n3,"is greater than",n1,"and",n2)
#
# # 10. Check whether a year is a leap year.
# y=int(input("enter a year:"))
# if (y%4==0 and y%100!=0) or y%400==0:
#     print(y,"is leap year")
# else:
#     print(y,"is not leap year")
#
# # 11. Check whether a person is eligible to vote (age ≥ 18).
# age=int(input("enter age:"))
# if age>=18:
#     print("congrats,you can vote")
# else:
#     print("see you next time")
#
# # 12. Calculate a student's grade based on marks.
# m=int(input("enter mark:"))
# if m>=90 and m<=100:
#     print('A grade')
# elif m>=80 and m<90:
#     print('B grade')
# elif m>=60 and m<80:
#     print('C grade')
# elif m>=30 and m<60:
#     print('D grade')
# else:
#     print('Fail')
#
# ---
#
# ## 3. Loops
#
# # 13. Print numbers from 1 to 10.
# for  i in range(1,11):
#     print(i,end=" ")
# print()
# #
# # 14. Print numbers from 10 to 1.
# for i in range(10,0,-1):
#     print(i,end=" ")
# print()
#
# # 15. Find the sum of the first `n` natural numbers.
# n=int(input("enter a no:"))
# sum=0
# for i in range(1,n+1):
#     sum=sum+i
# print(sum)
#
# # 16. Print the multiplication table of a given number.
# n=int(input("enter a no:"))
# for i in range(1,11):
#     print(n,'x',i,'=',n*i)
#
# # 17. Find the factorial of a number.
# n=int(input("enter a no:"))
# fact=1
# for i in range(1,n+1):
#     fact=fact*i
# print(fact)
#
# # 18. Count the number of digits in a number.
# n=int(input("enter a no:"))
# # l=len(n)
# # print(l)      #simple using len
# c=0
# while n>0:
#     c=c+1
#     n=n//10    #removes last digit (1234,123,12,1)
# print(c)
#
# # 19. Reverse a number.
# n=int(input("enter a number:"))
# # s=str(n)
# # print(s[::-1])    #using slice easy method
# rev=0
# while n>0:
#     digit=n%10
#     rev=rev*10+digit
#     n=n//10
# print("revere is",rev)
#
# # 20. Check whether a number is a palindrome.
# n=int(input("enter a no:"))
# s=str(n)
# r=s[::-1]
# if s==r:
#     print(n,"is palindrome")
# else:
#     print(n,"is not palindrome")        #using strings
#
# n=int(input("enter a no:"))
# temp=n
# rev=0
# while n>0:
#     d=n%10
#     rev=rev*10+d
#     n=n//10
# if temp==rev:
#     print(temp,"is palindrome")
# else:
#     print(temp,"is not palindrome")
#
# # 21. Find the sum of the digits of a number.
# n=input("enter a no:")
# sum=0
# for i in n:
#     sum=sum+int(i)
# print(sum)
from math import factorial


# # 22. Find all Armstrong numbers between 100 and 1000.
# for i in range(100,1000):
#     s=str(i)
#     l=len(s)
#     sum=0
#     for j in s:
#         sum=sum+int(j)**l
#     if sum==i:
#         print(i)
#
# # 23. Print all even numbers between 1 and 100.
# for i in range(1,100):
#     if i%2==0:
#         print(i,end=" ")
# print()
#
# # 24. Print all odd numbers between 1 and 100.
# for i in range(1,100):
#     if i%2!=0:
#         print(i,end=" ")
# print()
#
# ---
#
# ## 4. Patterns
#
# # 25. Print a square of `*`.
# #
# # ```
# # ****
# # ****
# # ****
# # ****
# for i in range(1,5):
#     for i in range(1,5):
#         print("*",end="")
#     print()
#
# # 26. Print a right triangle.
# #
# # ```
# # *
# # **
# # ***
# # ****
# # *****
# # ```
# for i in range(1,6):
#     for i in range(1,i+1):
#         print("*",end="")
#     print()
# #
# # 27. Print an inverted triangle.
# #
# # ```
# # *****
# # ****
# # ***
# # **
# # *
# # ```
# for i in range(5,0,-1):
#     for j in range(1,i+1):
#         print("*",end="")
#     print()
# #
# # 28. Print Floyd's Triangle.
# #
# # ```
# # 1
# # 2 3
# # 4 5 6
# # 7 8 9 10
# # ```
# k=1
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(k,end=" ")
#         k=k+1
#     print()
#
# ---
#
# ## 5. Strings
#
# # 29. Count the number of vowels in a string.
# s=input("enter a string:")
# v="aeiouAEIOU"
# c=0
# for i in s:
#     if i in v:
#         c+=1
# print("count of vowels:",c)

# # # 30. Check whether a string is a palindrome.
# s=input("enter a string:")
# r=s[::-1]
# if r==s:
#     print("palindrome")
# else:
#     print("not palindrome")

# # -----or------
#
# s=input("enter a string:")
# r=""
# for i in s:
#     r=i+r
# if r==s:
#     print("palindrome")
# else:
#     print("not palindrome")

# # 31. Count the number of words in a sentence.
# s=input("enter a sentence:")
# c=0
# for i in s.split():
#     c+=1
# print("number of words:",c)

# # 32. Reverse a string.
# s=input("enter a string:")
# print(s[::-1])

# # ---or----

# s=input("enter a string:")
# r=""
# for i in s:
#     r=i+r
# print(r)

# # 33. Count the occurrences of a character in a string.
# s=input("enter a string:")
# ch=input("enter a character:")
# print("Occurences=",s.count(ch))

# # --------or-------
#
# s=input("enter a string:")
# ch=input("enter a character:")
# c=0
# for i in s:
#     if i in ch:
#         c+=1
# print(c)
#
# ---
#
# ## 6. Lists
#
# # 34. Find the largest element in a list.
# l=[23,63,2,65,89,4,23,65]
# print(max(l))

# # -----or--------

# l=[23,63,2,65,89,4,23,65]
# l.sort()
# print(l[-1])

# # -----or------

# l=[23,63,2,65,89,4,23,65]
# m=0
# for i in l:
#     if i>m:
#         m=i
# print(m)

# # 35. Find the smallest element in a list.
# l=[23,63,2,65,89,4,23,65]
# print(min(l))

# # 36. Find the sum of all elements in a list.
# l=[3,6,11,25,15]
# s=0
# for i in l:
#     s=s+i
# print("Sum=",s)

# # 37. Find the average of a list.
# l=[2,4,1,5,3]
# count=0
# sum=0
# for i in l:
#     count=count+1
#     sum=sum+i
# avg=sum/count
# print("Average=",avg)

# # 38. Count even and odd numbers in a list.
# l=[1,2,3,4,5,7,6,9,8,2,43]
# even=0
# odd=0
# for i in l:
#     if i%2==0:
#         even=even+1
#     else:
#         odd=odd+1
# print("Even numbers=",even,"\nOdd numbers=",odd)

# # 39. Remove duplicate elements from a list.
# l=[2,4,5,3,7,7,4,2,9]
# new=[]
# for i in l:
#     if i not in new:
#         new.append(i)
# print(new)

# # ---------or--------
# l=[2,4,5,3,7,7,4,2,9]
# s=set(l)
# print(list(s))


# 40. Sort a list without using `sort()`.
#  -------------------------------------------------continue from here ------------------------------------------
# l=[2,4,3,1,7,6,9,10,8,5]
# min=min(l)
# print(min)
# new=[]
# for i in l:
#     if min<i:
#         min[i]=min[0]
#
#         new.append(i)
# print(new)

# ---
#
# ## 7. Functions
#
# 41. Write a function to add two numbers.
# def add():
#     num1=int(input("enter number1:"))
#     num2=int(input("enter number2:"))
#     sum=num1+num2
#     print("Sum =",sum)
# add()

# ---------or------------

# def add(a,b):
#     sum=a+b
#     return sum
# print(add(12,4))

# 42. Write a function to find the factorial of a number.
# def fact(n):
#     f=factorial(n)
#     return f
# print(fact(3))

# -------or-------
# def fact1():
#     n=int(input("Enter number:"))
#     f=1
#     for i in range(1,n+1):
#         i=i*f
#         f=i
#     return f
# print(fact1())

# 43. Write a function to check whether a number is prime.
# def prime(n):
#     if n%2==0:
#         print("not prime number")
#     else:
#         print("prime number")
# prime(8)

# # 44. Write a function to print prime numbers upto a given number
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

# # 45. Write a function to check whether a number is an Armstrong number.
# def arm(n):
#     sum=0
#     l=len(str(n))
#     for i in str(n):
#         sum=sum+int(i)**l
#     if sum==n:
#         return "Armstrong"
#     else:
#         return "not armstrong"
# print(arm(153))

# # 46. Write a function to find the maximum of three numbers.
# def max(n1,n2,n3):
#     if n1>n2 and n1>n3:
#         return n1
#     elif n2>n1 and n2>n3:
#         return n2
#     else:
#         return n3
# print("Maximum of 3 numbers is ",max(2783,458,65))
#
# # -----------or-----------
# def max3(n1,n2,n3):
#     return max(n1,n2,n3)
# print(max3(34,56,43))
#
# ---
#
# ## 8. Mixed Practice
#
# 47. Guess the number game.
# 48. Simple calculator using `if-elif`.
# 49. ATM menu (Deposit, Withdraw, Balance).
# 50. Student marks calculator.
# 51. Number guessing game with 3 chances.
#
# ### Challenge Questions
#
# * Print all prime numbers between 1 and 100.
# * Find the Fibonacci series up to `n` terms.
# * Find the GCD and LCM of two numbers.
# * Count uppercase, lowercase, digits, and special characters in a string.
# * Create a simple password checker.
#


# def spy(n):
#     sum=0
#     p=0
#     for i in str(n):
#         sum=sum+int(i)
#         p=p*int(i)
#     if sum==p:
#         return "spy number"
#     else:
#         return "not spy"
#
# n=int(input("enter a number:"))
# s=spy(n)
# print(s)


