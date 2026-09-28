
# # # # ================================LAMBDA===========================

# #product of a number
# a=lambda x:x*x
# print(a(5))

# #sum of 2 numbers
# add=lambda a,b:a+b
# print(add(20,10))

# # product of 3 numbers
# p=lambda a,b,c:a*b*c
# print(p(2,3,4))

# # cube of a number
# cube=lambda a:a**3
# print(cube(5))

# #first letter of a string
# fs=lambda s:s[0]
# print(fs("Python"))

# #length of a string
# ls=lambda s:len(s)
# print(ls("hello "))

# #reverse of a string
# rev=lambda r:r[::-1]
# print(rev("world"))

# #name value from a dictionary
# d={'name':'arun','age':21}
# name=lambda d:d['name']
# print(name(d))

# #second element from a list
# se=lambda s:s[1]
# print(se([10,20,48,32]))

# #add 10 to a number
# ten=lambda n:n+10
# print(ten(30))


# # # # ==============================MAP=================================

# # given a list
# l=[1,2,3,4]
# print(list(map(lambda x:x**2,l)))
# print(tuple(map(lambda x:x**2,l)))
# print(set(map(lambda x:x**2,l)))


# #create a new list of cubes
# l=[1,2,3,4]
# print(list(map(lambda a:a**3,l)))

# #create a new list of square roots
# l=[25,36,81,100]
# print(list(map(lambda a:a*0.5,l)))

# #create a new list of lengths
# colors=['red','green','blue','yellow','black']
# print(list(map(lambda l:len(l),colors)))

# #create a new list of first characters
# print(list(map(lambda s:s[0],colors)))

# #create a new list of last characters
# print(list(map(lambda s:s[-1],colors)))

# #create a new list of reverse of each elemnt
# print(list(map(lambda s:s[::-1],colors)))


# #Given a list
# l=[23,78,12,56]
# #Add 10 to each element in the given sequence
# print(list(map(lambda x:x+10,l)))


# ##given a list of dictionaries
l=[{'empid':100,'name':'arun','salary':20000,'email':'arun@gmail.com'},
   {'empid':101,'name':'amal','salary':25000,'email':'amal@gmail.com'},
   {'empid':102,'name':'anu','salary':30000,'email':'anu@gmail.com'}]

# # create a new list of emails
print(list(map(lambda e:e['email'],l)))




# # # # =================================FILTER=================================


# l=[1,2,3,4,5,6,7,8,9,10]
# print(list(filter(lambda x:x%2==0,l)))

# #given a list
# l=[23,45,67,12,89,70]
# #filter even values greater than 50
# print(list(filter(lambda a:a%2==0 and a>50,l)))

# #given a list
# colors=['red','green','blue','yellow','orange']
# # filter the color whose length is greater than 5
# print(list(filter(lambda s:len(s)>5,colors)))

# #filter the color containing letter 'n'
# print(list(filter(lambda s:"n" in s,colors)))



# # # # =============================REDUCE==========================

# import functools
# l=[1,2,3,4]
# print(functools.reduce(lambda x,y:x+y,l,0))



#############################################################


