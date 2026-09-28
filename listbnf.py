# #given a list
# l=[1,2,2,3,4,4,5,6]
# # create a new dictionary where keys are numbers and values are number occurence of each number
# # new={i:l.count(i) for i in l}
# # print(new)
#
# # -------------
# new={}
# for i in l:
#     new[i]=l.count(i)
# print(new)
#
# # given a list
# l=[11,34,78,23,90,65]
# # find largest no
# print("largest no:",max(l))
#
# # find second largest no
# l.sort()
# print("second largest no:",l[-2])
#
# # find smallest no
# print("smallest no:",min(l))
#
# # find second smallest no
# print("second smallest:",l[1])
#
#
# # given a list
# l=[['arun',23,30000],['amal',25,50000],['anu',27,40000]]
# # maximum salary
# maximum=max([i[2] for i in l ])
# print(maximum)
#
# # minimum salary
# minimum=min([i[2] for i in l])
# print(minimum)


# given a list
l=[23,45,67,12,90,78]
# find largest no without using built in functions
max=l[0]
for i in l:
    if i>max:
        max=i
print("maximum",max)

#smallest no
min=l[0]
for i in l:
    if i<min:
        min=i
print("minimum",min)