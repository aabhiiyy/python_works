# ##
s="hello"
# for i in s:
#     print(i)
#
# #break
# for i in s:
#     if i=='l':
#         break
#     print(i)
#
# #continue
# for i in s:
#     if i=='l':
#         continue
#     print(i)

#pass
# for i in s:
#     if i=='l':
#         pass
#     print(i)

#-------------------------------------------------------------

## 1.given a list of numbers
# l=[25,67,34,78,17,44,82]
# #print all numbers
# # for i in l:
# #     print(i)
# #stops the loop when i>50
# for i in l:
#     if i>50:
#         break
#     print(i)
#
# #skips all even numbers
# for i in l:
#     if i%2==0:
#         continue
#     print(i)

## 2.Given a list
colors=['red','green','yellow','blue','orange','black']
# #print all colors
# for i in colors:
#     print(i,end=' ')
# print()

# #print those colors starting with 'b' #blue black
# for i in colors:
#     if i[0]=='b':
#         print(i,end=" ")
# print()

# #print the first color starting with 'b' #blue
# for i in colors:
#     if i[0]=='b':
#         print(i, end=" ")
#         break
# print()

# #skips all colors starting with 'b'
# for i in colors:
#     if i[0]=='b':
#         continue
#     print(i,end=" ")
# print()

## 3.Given
s="python coding is easy and fun"
#print all characters upto a specific character(including that character)
for i in s:
    print(i,end=" ")
    if i=='a':
        break
    # print(i,end=" ")