__author__ = 'wanjugu'

# Ready! Set! Fire... but where should you fire?
#
# The battlefield is 3x3 wide grid. HQ has already provided you with an array for easier computing:
#
# grid = ['top left',    'top middle',    'top right',
#         'middle left', 'center',        'middle right',
#         'bottom left', 'bottom middle', 'bottom right']
# HQ radios you with 'x' and 'y' coordinates. x=0 y=0 being 'top left' part of the battlefield;
#
# Your duty is to create a function that takes those Xs and Ys and return the correct grid sector to be hit.
#
# fire(0,0) # 'top left'
# fire(1,2) # 'bottom middle'
# etc.
# Notice the grid is a monodimensional array, good luck!

# def fire(x,y);
#Creating matrices

from numpy import array
import numpy as np #for matrix/array creation
A = array(([3, 8, 5],\
           [6, 4, 7]))

# print (A)

x = np.arange(10)
print (x)

#You can index as usual
# print(x[2])

#multidimnsional arrays
x.shape = (2,5)
print (x)
print (x[0]) #prints the first row
print (x[1]) #prints the second row

print (x[1,3]) #prints item at index [3] in the second row [1]

# Example
k = np.arange(10)
key_num = k[1:]
print(key_num)

key_num.shape = (3,3)
print(key_num)

grid = array ((["top left", "top middle", "top right"],\
              ["middle left", "center middle", "center right"],\
              ["bottom left", "bottom middle", "bottom right"]))

print (grid)



