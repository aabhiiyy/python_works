# #Create a package named Shapes containing modules circle.py  and
# rectangle.py

# define functions to calculate the area and perimeter of  circle and rectangle.

# write a program mymodule.py to import all these functions from the circle and
# rectangle modules and perform required operations.

def circle(r):
    area=3.14*(r**2)
    perimeter=2*(3.14*(r**2))
    print("area of circle=",area)
    print("perimeter of circle=",perimeter)
# circle(5)