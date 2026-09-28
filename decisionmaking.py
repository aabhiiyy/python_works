##write a program to check whether the number is even

# n=int(input("enter a number: "))
# if n%2==0:
#    print("number is even")

##write a program to check whether the number is positive or negative

# n=int(input("enter a number: "))
# if n>0:
#     print("Number is positive")
# else:
#     print("Number is negative")

##write a program to check whether the number is even or odd

# n=int(input("enter a number: "))
# if n%2==0:
#    print(n,"is even number")
# else:
#     print(n,"is odd number")
    # print(f"{n} is odd number")

##check whether the number is divisible by 3

# n=int(input("enter a number: "))
# if n%3==0:
#     print(n,"is divisible by 3")
# else:
#     print(n,"is not divisible by 3")

##write a program to display a name if the entered name contains letter 'n' else print 'no'

# name=(input("enter a name:"))
# if 'n' in name:
#     print("Name is",name)
# else:
#     print('no')

##write a program to display a name if the entered name starts with letter 'n' else display 'no'

# name=input("Enter a name:")
# if name[0]=='n':
#     print("name is",name)
# else:
#     print('no')

##write a program to display a location name if the entered location contains the word 'land' else print 'no'

# loc=input("enter a loction:")
# if 'land'in loc:
#     print('place is',loc)
# else:
#     print('no')

##write a program to check whether the number is divisible by 5 and ends with 5

# n=int(input("enter a number:"))
# if n%5==0 and n%10==5:
#     print(n,'is divisible by 5 and ends with 5')
# else:
#     print('no')

##write a program to find the greatest of two numbers
##write a program to find the greatest of three numbers

# n1=int(input("enter first number:"))
# n2=int(input("enter second number:"))
# n3=int(input("enter third number:"))
# if n1>n2 and n1>n3:
#     print(n1,"is greater than",n2,"and",n3)
# elif n2>n1 and n2>n3:
#     print(n2,"is greater than",n1,"and",n3)
# else:
#     print(n3,"is greater than",n1,"and",n2)

##write a program to check whether the number is positive or negative or zero

# n=int(input("enter a number: "))
# if n>0:
#     print(n,"is positive")
# elif n<0:
#     print(n,"is negative")
# else:
#     print(n,"is zero")

##write a program to check whether a person is eligible to vote or not

# age=int(input("enter age:"))
# if age>18:
#     print("you are eligible to vote")
# else:
#     print("you are not eligible to vote")

##write a prggrm to check whether a number is even or odd or invalid


n=int(input("enter a number: "))
if n%2==0:
   print(n,"is even number")
elif n%2!=0:
    print(n,"is odd number")
else:
    print("Invalid credentials")
