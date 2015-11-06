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

##############################################################
#### Introduction to Matrices #####
#Creating matrices
#
# from numpy import array
# import numpy as np #for matrix/array creation
#
# A = array(([3, 8, 5],\
#            [6, 4, 7]))
#
# # print (A)
#
# x = np.arange(10)
# print (x)
#
# #You can index as usual
# # print(x[2])
#
# #multidimnsional arrays
# x.shape = (2,5)
# print (x)
# print (x[0]) #prints the first row
# print (x[1]) #prints the second row
# print (x[1,3]) #prints item at index [3] in the second row [1]
#
# # Example
# k = np.arange(10)
# key_num = k[1:]
# print(key_num)
#
# key_num.shape = (3,3)
# print(key_num)
#
# ##############################################################

##-----------------------------------------------------------------------##
# Actual Calculation



from numpy import array
import numpy as np #for matrix/array creation

def fire(x,y):
    grid = np.array(["top left", "top middle", "top right",
                     "middle left", "center", "middle right",
                     "bottom left", "bottom middle", "bottom right"])

    # converting one dimensional grid to (3x3) matrix grid_m
    grid_m = np.zeros((0,3))  # empty (3x3) matrix

    for i, item in enumerate(grid):
        if (i%3==0):
            #Splits grid after every third item
            row = [grid[i:i+3]]
            grid_m = np.concatenate((grid_m, row))

    # print(grid_m)

    row_0 = grid_m[0]
    row_1 = grid_m[1]
    row_2 = grid_m[2]
    print (row_1)

    for z in range (0,3):
        if (y != z):
            position = "Error: Input values between 0 and 2"
            print(position)
            break
        elif (y == z):
            if (x == 0):
                position = row_0[y]
            elif (x == 1):
                position = row_1[y]
            elif (x == 2):
                position = row_2[y]
            else:
                position = "Error: Input values between 0 and 2"
            print (position)


fire(2,1)
