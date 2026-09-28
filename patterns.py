# # print
# # 10 10 10
# # 20 20 20
# # 30 30 30
#
# l=[10,20,30]
# for i in l:
#     for j in range(1,4):
#         print(i,end=" ")
#     print()
#
# # 1 1 1 1
# # 2 2 2 2
# # 3 3 3 3
#
# l1=[1,2,3]
# for i in l1:
#     for j in range(1,5):
#         print(i,end=" ")
#     print()
#
# 1 2 3 4
# 1 2 3 4
# 1 2 3 4
# l1=[1,2,3]
# for i in range(1,4):
#     for j in range(1,5):
#         print(j,end=" ")
#     print()
#
#
# for i in range(1,4):
#     for j in range(1,5):
#         print('*',end=" ")
#     print()

# l=[['lion','tiger'],['cat','elephant']]
# for i in l:
#     print(i)
#     for j in i:
#         print(j,end=" ")
#     print()

# #1.given a list
# names=['kelly','alan','jeny']
# # print
# # kelly kelly kelly
# # alan alan alan
# # jeny jeny jeny
# for i in names:
#     for j in range(1,4):
#         print(i,end=" ")
#     print()

# #2.given 2 lists
# n=[1,2,3]
# q=['what','when','why']
# # print
# # 1
# # what when why
# # 2
# # what when why
# # 3
# # what when why
# for i in n:
#     print(i)
#     for j in q:
#         print(j,end=" ")
#     print()
#


# -----------------------------------------------------------------


# #3.given a list
# d=[{'id':101,'name':'arun','age':23},
#    {'id':102,'name':'amal','age':24},
#    {'id':103,'name':'anu','age':25}]
# #print each student details
# # id name age
# print('ID  NAME AGE')
# for i in d:
#     for j in i.values():
#         print(j,end=" ")
#     print()
#
# # items
# d={'id':101,'name':'arun','age':23}
# for i,j in d.items():
#     print(i,j)


## ---------------------patern------------------------

# # *
# # * *
# # * * *
# # * * * *
# for i in range(1,5):
#     for j in range(1,i+1):
#         print('*',end=" ")
#     print()
# print()
#
# # or
# for i in range(1,4):
#     print('* ' * i)
#
#
# # 1
# # 2 2
# # 3 3 3
# # 4 4 4 4
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(i,end=" ")
#     print()
# print()
#
# # 1
# # 1 2
# # 1 2 3
# # 1 2 3 4
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()
# print()
#
# # *
# # * * *
# # * * * * *
# # * * * * * * *
# for i in range(1,8,2):
#     for j in range(1,i+1):
#         print('*',end=" ")
#     print()
# print()
#
# # * * * *
# # * * *
# # * *
# # *
# for i in range(4,0,-1):
#     for j in range(i):
#         print('*',end=" ")
#     print()
# print()
#
# # or
# for i in range(4,0,-1):
#     print('* '*i)
# print()


# --------------------------prime no-----------------------------------


# l=[23,45,78,90,12,13,91]
# # print all prime numbers
# for i in l:
#     if i>1:
#         for j in range(2,i):
#             if i%j==0:
#                 # print("not prime")
#                 break
#         else:
#             print(i)
#     else:   #number 1 or 0 or negative
#         print("number is neither prime nor composite")


# # #find all prime numbers in the range(1,100)
# for i in range(1,100):
#     if i>1:
#         for j in range(2,i):
#             if i%j==0:
#                 break
#         else:
#             print(i,end=" ")
#     else:
#         print("number is neither prime nor composite")
# print("\n")
#

# ##find all armstrong numbers in the range(100,1000)
# for i in range(100, 1000):
#     sum = 0
#     for j in str(i):
#         sum = sum + int(j) ** 3
#     if sum == i:
#         print(i)
#
# # or
#
# # for i in range(100,1000):
# #     if (i//100)**3+((i//10)%10)**3+(i%10)**3==i:
# #         print(i)


# -----------------------------------------------------------

#
# #1 2 3 4 5
# #1 2 3 4 5
# #1 2 3 4 5
# #1 2 3 4 5
#
# for i in range(1,5):
#     for j in range(1,6):
#         print(j,end=" ")
#     print()

# # * * * *
# # * * *
# # * *
# # *
#
# for i in range(4,0,-1):
#     for j in range(i):
#         print('*',end=" ")
#     print()

# # 1
# # 2 3
# # 4 5 6
# # 7 8 9 10
#
# k=1
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(k,end=" ")
#         k=k+1
#     print()

# # A
# # B C
# # D E F
# # G H I J
#
# k=ord('A')
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(chr(k),end=" ")
#         k=k+1
#     print()
#
# # A
# # B B
# # C C C
# # D D D D
#
# k=ord('A')
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(chr(k),end=" ")
#     k=k+1
#     print()
#
# # A
# # A B
# # A B C
# # A B C D
#
# for i in range(1,5):
#     k = ord('A')
#     for j in range(1,i+1):
#         print(chr(k),end=" ")
#         k=k+1
#     print()

# # 1 1 1 1
# # 2 2 2 2
# # 3 3 3 3
# # 4 4 4 4
#
# for i in range(1,5):
#     for j in range(1,5):
#         print(i,end=" ")
#     print()
#
# # 1 0 0 0
# # 0 2 0 0
# # 0 0 3 0
# # 0 0 0 4
#
# for i in range(1,5):
#     for j in range(1,5):
#         if i==j:
#             print(i,end=" ")
#         else:
#             print(0,end=" ")
#     print()
#
# # 1
# # 1 0
# # 1 0 1
# # 1 0 1 0
#
# for i in range(1,5):
#     for j in range(1,i+1):
#         if j%2==0:
#             print(0,end=" ")
#         else:
#             print(1,end=" ")
#     print()

# # 0
# # 0 1
# # 0 1 2
# # 0 1 2 3
# # 0 1 2 3 4
#
# for i in range(0,5):
#     for j in range(0,i+1):
#         print(j,end=" ")
#     print()
#
# # h
# # h e
# # h e l
# # h e l l
# # h e l l o
# # h e l l o
# # h e l l o   h
# # h e l l o   h i
#
# s="hello hi"
# # for i in range(1,5):   #static range
# for i in range(len(s)):
#     for j in range(0,i+1):
#         print(s[j],end=" ")
#     print()

# #       *
# #     * *
# #   * * *
# # * * * *
#
# k=3*2
# for i in range(1,5):
#     for p in range(1,k+1):
#         print(end=" ")
#     for j in range(1,i+1):
#         print("*",end=" ")
#     k=k-2
#     print()
#
#  #    *
#  #   * *
#  #  * * *
#  # * * * *
#
# k=3*2
# for i in range(1,5):
#     for p in range(1,k+1):
#         print(end=" ")
#     for j in range(1,i+1):
#         print("*",end=" ")
#     k=k-1
#     print()
#
# #       *
# #     *   *
# #   *   *   *
# # *   *   *   *
#
# k=3*2
# for i in range(1,5):
#     for p in range(1,k+1):
#         print(end=" ")
#     for j in range(1,i+1):
#         print("*",end="   ")
#     k=k-2
#     print()

# #       *
# #     *   *
# #   *   *   *
# # *   *   *   *
# #   *   *   *
# #     *   *
# #       *
#
#
# k=3*2
# for i in range(1,5):
#     for p in range(1,k+1):
#         print(end=" ")
#     for j in range(1,i+1):
#         print("*",end="   ")
#     k=k-2
#     print()
#
# k=2
# for i in range(3,0,-1):
#     for p in range(1,k+1):
#         print(end=" ")
#     for j in range(1,i+1):
#         print("*",end="   ")
#     k=k+2
#     print()
#
# #       1
# #     1   2
# #   1   2   3
# # 1   2   3   4
# #   1   2   3
# #     1   2
# #       1
#
# k=3*2
# for i in range(1,5):
#     for p in range(1,k+1):
#         print(end=" ")
#     for j in range(1,i+1):
#         print(j,end="   ")
#     k=k-2
#     print()
#
# k=2
# for i in range(3,0,-1):
#     for p in range(1,k+1):
#         print(end=" ")
#     for j in range(1,i+1):
#         print(j,end="   ")
#     k=k+2
#     print()



