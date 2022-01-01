# version of python

import sys
print("The version of python is")
print (sys.version)


# Poem

print('Twinkle, twinkle. little star')
print('         How I wonder what you are!')
print('                 Up above the world so high,')
print('                 Like a diamond in the sky.')
print('Twinkle, twinkle, little star,')
print('        How I wonder what you are')

# The value of current date and time

import datetime
now = datetime.datetime.now()
print ("Now date and time is: ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))

# Area of circle

PI = 3.14
radius = float(input('Enter the radius of a circle: '))
area = PI * radius * radius
print(" Area Of Circle = %.2f" %area)

# First and last name

q = input ('Enter first name')
v = input ('Enter last name')

print(v,q)

# Addtion of two inputs

d = int(input('Enter first number'))
e = int(input('Enter second number'))
c = d+e
print(c)








