#declare a list of 5 colors
lst=['red','white','blue','green','pink']
print(lst)
#add a new color yellow to the list
lst.append('yellow')
print(lst)
#change the second color to black
lst[1]='black'
print(lst)
#print the list in reverse order
print(lst[::-1])
#print the second last color
print(lst[-2])
#print the number of color
print(len(lst))
#print the updated list
print(lst)