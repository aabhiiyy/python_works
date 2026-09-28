# l=[1,2,3,4]
# new=[i**2 for i in l]
# print(new)
#
# l=[1,2,3,4]
# new=[i**3 for i in l]
# print(new)
#
# l=[1,2,3,4]
# new=[5 for i in l]
# print(new)
#
#
# #given a list
# l1=[23,56,34,12,89,90,24]
# #print even numbers
# new=[i for i in l1 if i%2==0]
# print(new)
#
# #print i>50 in the above list
# new=[i for i in l1 if i>50]
# print(new)
#
#
# # Given a list
# l=[12,45,34,67,90]
# # create a new list with even values
# new=[i for i in l if i%2==0]
# print(new)
#
# #create a new list with values greater than 50
# new=[i for i in l if i>50]
# print(new)
#
#
# #Given  a list
# colors=['red','green','blue','orange']
# # create a new list with first letter of each color
# new=[i[0] for i in colors]
# print(new)
#
# # create a new list with length of each color
# new=[len(i) for i in colors]
# print(new)
#
#
# #create a new list of cubes
# l=[1,2,3,4]
# new=[i**3 for i  in l]
# print(new)
#
import math          #math.sqrt


# #create a new list of square roots
# l=[25,36,81,100]
# # new=[int(math.sqrt(i)) for i in l]
# new=[int(i**0.5) for i in l]             #root(x)=x^1/2 , 1/2=0.5
# print(new)


# #create a new list of lengths
# colors=['red','green','blue','yellow','black']
# new=[len(i) for i in colors]
# print(new)
#
# #create a new list of first characters
# new=[i[0] for i in colors]
# print(new)
#
# #create a new list of last characters
# new=[i[-1] for i in colors]
# print(new)
#
# #create a new list of reverse of each element
# new=[i[::-1] for i in colors]
# print(new)
#
#
# #Given a list
# l=[23,78,12,56]
# #Add 10 to each element in the given sequence
# new=[i+10 for i in l]
# print(new)
#
#
# ##given a list of dictionaries
# l=[{'empid':100,'name':'arun','salary':20000,'email':'arun@gmail.com'},
#    {'empid':101,'name':'amal','salary':25000,'email':'amal@gmail.com'},
#    {'empid':102,'name':'anu','salary':30000,'email':'anu@gmail.com'}]
#
# # # create a new list of emails
# new=[i['email'] for i in l]
# print(new)
#
#
# # # #create a new list with square root of each element
# l=[25,16,9,36]
# new=[math.sqrt(i) for i in l]
# print(new)
#
#
# # #Given a dictionary
# d={'arun':25,'amal':34,'akhil':26,'anu':21}
# # # create a list of names
# new=[i for i in d]
# print(new)
#
# # # create a list of marks
# # new=[d[i] for i in d]
# new=[i for i in d.values()]
# print(new)


# # #Given a list
# l=[23,56,12,89,-34,-23,-67,-43,9.7,4.5,'hello','world']
# # #create a list of string values
# new=[i for i in l if type(i)==str]
# print(new)
#
# # #create a list of floats
# new=[i for i in l if type(i)==float]
# print(new)
#
# # #create a list of positive numbers
# new=[i for i in l if (type(i)==int or type(i)==float) and i>0]
# new=[i for i in l if type(i)!=str and i>0]
# print(new)
#
#
# # #Given a list
# fruits=['apple','orange','pineapple','avocado','grapes']
# # #create a new list with elements whose length is greater than 6
# new=[i for i in fruits if len(i)>6]
# print(new)


# #create a new list with elements whose value is divisible by 3 in range(1,101)
# new=[i for i in range(1,101) if i%3==0]
# print(new)

# Given
# s="python coding  is easy and fun"
# # create a new list with only vowels
# v="aeiouAEIOU"
# new=[i for i in s if i in v]
# new=[i for i in s if i in "aeiouAEIOU"]
# print(new)

# #given
# s="python coding  is easy and fun"
# # create new set
# new={i for i in s if i in "aeiouAEIOU"}
# print(new)

# # given
# # create new dictionary where keys are elements and values are its square
# l=[1,2,3,4]
# new={i:i**2 for i in l}
# print(new)

#given a list
l=[10,20,30,40]
#create a new dictionary where keys are indexes and values are numbers
new={i:l[i] for i in range(0,4)}
# new={i:l[i] for i in range(0,len(l))}
print(new)


# --------------------split()-----------------------


s="hello world"
# #----characters
# for i in s:
#     print(i)
#------words
for i in s.split():
    print(i)

s="python coding is easy and fun"
new={i:len(i) for i in s.split()}
print(new)