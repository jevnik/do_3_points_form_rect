import math
import numpy as np
import time
import sys


def p2p_distance(a, b) -> float:
        '''
        Calculates euclidean distance between two points (a and b) defined as numpy.array. Points can have n dimensions
        '''
        distance = []
        for c1, c2 in zip(a, b):
            distance.append((c1 - c2) ** 2) # Calculates distance of points on one axis and ads to a list

        return math.sqrt(sum(distance))

def data_preprocess(points:list):
    '''
    Takes in raw list with point cooridantes by "," and stores it into a numpy array as floats for easy manipulation
    '''
    for i in range(len(points)):
        points[i] = points[i].split(", ")

    for i in range(len(points)):
        points[i] = np.array([float(i) for i in points[i]])

    shape_points = points[:-1].copy()
    x_point = points[-1].copy()

    if not np.all(shape_points[0] == 0):
    # Moves body to the origin if the first point is not at the origin
        a = shape_points[0].copy()
        for i in range(len(shape_points)):
            shape_points[i] -= a
    shape_points = np.array(shape_points[1:]) # Drops first point since its now in origin

    return shape_points, x_point

def is_preprendicular(shape_points,n) -> bool:
    '''
    checks if every vectors is perpendicular to all others
    '''
    dot_product = 0
    for i in range(n):
        for j in range(n):
            if i == j:
                pass
            else:
                dot_product += np.dot(shape_points[i],shape_points[j].T)

    return dot_product == 0

def is_inside_of_shape(shape_points,x_point) -> bool:
    '''
    checks if point is inside of a shape
    '''
    dim_coords = []
    for dim in range(len(x_point)):
        for p in shape_points:
            dim_coords.append(p[dim]) # Stores coordinates of all points on one axis 
        
        if min(dim_coords) <= x_point[dim] <= max(dim_coords): # Point is consireded inside of a shape if it is on the border of the shape
            dim_coords = []
            continue
        else:
            dim_coords = []
            return False
    
    return True

def diagonal_length(shape_points):
    '''
    calculates length of a diagonal
    '''
    lines_len = []
    for i in range(len(shape_points)): # Measures distance between all points
        lines_len.append(p2p_distance(shape_points[i-1], shape_points[i]))
    
    return max(lines_len)



with open(r"input.txt", "r") as input_data: # Reads the file
    points = input_data.read().split("\n")


shape_points, x_point = data_preprocess(points)

n_of_dims = len(shape_points)

if is_preprendicular(shape_points,n_of_dims):
    if n_of_dims == 2:
        print("Points make a rectangle")
    elif n_of_dims == 3:
        print("Points make a right angle paralelopiped")
    else:
        print("Points make an n dimensional right angle shape")
else:
    print("Points dont make a right angle shape")
    print("Program will now exit")
    for i in range(5):
        time.sleep(0.5)
        print(".")
    sys.exit()

if is_inside_of_shape(shape_points,x_point):
    print("Point is inside of the shape")
else:
    print("Point is outside of the shape")

print("Length of a diagonal is:", diagonal_length(shape_points))
input("Press any key to exit")
