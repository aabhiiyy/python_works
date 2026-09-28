#
# def fun(n,a):
#     print("name:",n)
#     print("age:",a)
# fun("ammu",21)                 #positional argument
# #
# fun(n="anu",a=21)                      #keyword argument
# fun(a=23,n="appu")                     #keyword argument

# def fun(n,a=25):                       #default argument
#     print("name:",n)
#     print("age:",a)
# fun("anoop",32)
# # fun("sanju")                         #default value of age is 25 it will display

#------------------------variable length arguments

# def fun(*args):                    #positional arbitary
#     print(args)
# fun(10,20)
# fun(10,20,30,40)
#
# def fun(**kwargs):                #keyword arbitary
#     print(kwargs)
# fun(a=10,b=20,c=30)
# fun(n=1,b=2,d=4)

#define a function to find the sum of numbers using arbitary arguments type
#
def add(*args):
    s=0
    for i in args:
        s=s+i
    print(s)
    # pass
add(10,20)
add(1,2,3,4,5)

print(sum)
def add(*args):
    s=0
    for i in args:
        s=s+i
    return s
    # pass
sum=add(10,20)
# add(1,2,3,4,5)
print(sum)



#----------------------------------buit in functions----------------


# import math
# print(round(7.895,2))
# print(abs(-100))
# print(abs(100))
# print((divmod(10,2)))
# print(math.ceil(8.6))              #9  nxt int
# print(math.floor(8.6))             #8  previous int
# print(math.factorial(12))
# print(math.pow (2,3))
# print(complex(math.pow(3,4)))
# print(int(math.pow(2,3)))
