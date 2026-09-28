#write a program to check whether a no. is armstrong no.
n=int(input("enter a no:"))
s=str(n)
l=len(s)
sum=0
for i in s:
    sum=sum+int(i)**l
if(sum==n):
    print("armstrong")
else:
    print("not armstrong")


# #factors of a number
# num=int(input("enter a number:"))
# for i in range(1,num+1):
#     if num%i==0:
#         print(i,end=" ")
# print()

# ##for-else in normal case
# for i in range(1,6):
#     print(i)
# else:
#     print("hello")


# ##for-else in break
# for i in range(1, 6):
#     if i==3:
#         break
#     print(i)
# else:
#     print("hello")



# ##check whether a no is prime or not
# n=int(input("enter a no:"))
# if n>1:
#     for i in range(2,n):
#         if n%i==0:
#             print("not prime")
#             break
#     else:
#         print("prime")
# else:   #number 1 or 0 or negative
#     print("number is neither prime nor composite")