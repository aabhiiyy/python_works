# s={1,2,3,4}
# t={4,6,5,7,3}
#
# a=s.union(t)
# print(a)
# b=s.intersection(t)
# print(b)
# c=s.difference(t)
# print(c)
# d=t.difference(s)
# print(d)
# e=s.symmetric_difference(t)
# print(e)
#

# # given a list
l=[1,1,2,3,3,4]
# remove the duplicates
print(set(l))
# # given a list
l=[1,1,2,3,3,4]
# remove duplicates without using set() (order should be preserved)
new=[]
for i in l:
    if i not in new:
        new.append(i)
print(new)

# # given a list
l1=[13,27,30,42,57]
l2=[13,57,89,33,80]
# find the common elements
h=set(l1)
print(h)
k=set(l2)
print(k)
f=h.intersection(k)
print(f)
      # or
s1=set(l1)
s2=set(l2)
print(s1.intersection(s2))