# #Create a package named Calculator containing single module operations.py

#
# in operations.py define
# add() --addition of two numbers
# sub()
# mul()
# div()

# write a program mymodule.py to import all these functions from the operations
# module and perform required operations using inputs:


def add(a,b):
    sum=a+b
    print("sum=",sum)
    # return sum
# add()

def sub(a,b):
    s=a-b
    print("sub=",s)
# sub(14,6)

def mul(a,b):
    p=a*b
    print("product=",p)
# mul(5,4)

def div(a,b):
    d=a/b
    print("division=",d)
# div(20,5)