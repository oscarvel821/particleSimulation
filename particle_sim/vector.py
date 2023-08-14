from math import cos, sin, sqrt, atan2, pi
import random

def rotatePoint(point, angle):
    x, y = point
    c = cos(angle)
    s = sin(angle)

    return [x * c - y * s, x * s + y * c]

def addVector(vector1, vector2):
    '''Returns back a Vector with magnitude and direction'''
    x1, y1 = getComponents(vector1)
    x2, y2 = getComponents(vector2)

    x = x1 + x2
    y = y1 + y2

    return compToVector(x, y)

def addVectorWithScaler(vector1, vector2, scaler):
    '''Returns back a Vector with magnitude and direction'''
    x1, y1 = getComponents(vector1)
    x2, y2 = getComponents(vector2)

    x = x1 + x2 * scaler
    y = y1 + y2 * scaler

    return compToVector(x, y)

def getComponents(vector):
    x_comp = vector[0] * cos(vector[1])
    y_comp = vector[0] * sin(vector[1])

    return [x_comp, y_comp]

def compToVector(x, y):
    magnitude = sqrt(x ** 2 + y ** 2)
    direction = atan2(y, x)

    return [magnitude, direction]

def dotProduct(vector1, vector2):
    return vector1[0] * vector2[0] + vector1[1] * vector2[1]

def keepAngleRange(angle):
    if angle < 0:
        while angle < 0:
            angle += 2*pi
    if angle > 2*pi:
        while angle > 2 * pi:
            angle -= 2*pi
    
    return angle

def wrappedPosition(position, screen_width, screen_height):
    if position[0] > screen_width:
        position[0] = 0
    elif position[0] < 0:
        position[0] = screen_width
    
    if position[1] > screen_height:
        position[1] = 0
    elif position[1] < 0:
        position[1] = screen_height

    return position