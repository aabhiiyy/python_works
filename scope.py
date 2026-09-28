# # global     - can be used anywhere in the program


# x=20
# print("outside function" ,x)
#
# def abc():
#     print("inside function" ,x)
# abc()


# # local       - can be used only inside the block
#
#
# def bcd():
#     x=22
#     print("inside function" ,x)
# bcd()
# # print("outside function" ,x)            #error


# # nonlocal/enclosing

# def f():
#     global x                   # making x as global variable to use x value in g function
#     x=30
#     print("inside f funtion",x)
# def g():
#     y=40
#     print("x value from f function",x)
#     print("inside g function",y)
#
# f()
# g()


# # nonlocal/enclosing

def outer():
    x=23        #nonlocal
    print("outer",x)
    def inner():
        y=33       #local
        print("inside",y)
        print("inner",x)
        return
    inner()
outer()

