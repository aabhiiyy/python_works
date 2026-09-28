##4,9,14,19,24,29,34,39
# i=4
# while(i<=39):
#     print(i,end=" ")
#     i=i+5
# print("\n")
# ##sum of series 1,3,5,7,9,11
# i=1
# sum=0
# while(i<=11):
#     sum=sum+i
#     i=i+2
# print(sum)
#
# ## product of numbers that are divisible by 3 and 5 in the range of(1,50)
# i=1
# p=1
# while(i<=50):
#     if i%3==0 and i%5==0:
#         p=p*i
#     i=i+1
# print(p)
#
# ##count of 3 digits numbers that are divisible by 7
# i=100
# count=0
# while(i<1000):
#     if i%7==0:
#         count=count+1
#     i=i+1
# print('count=',count)
#
# ##factorial of a no.
# #multiplication of a no. upto 10
# i=1
# fact=1
# n=int(input("enter a no:"))
# while(i<=n):
#       fact=fact*i
#       i=i+1
# print(fact)

i=1
n=int(input("enter a no:"))
while(i<=10):
    # print(i*n)
    print(n,'*',i,'=',n*i)
    i=i+1