from types import new_class
import math
import data

# Write your functions for each part in the space below.

# Part 1
def first_element(values:list[list[int]])->list[int]:
    #checks if list is empty by making sure there is a value in the list, if not then it doesn't include list
    checkForEmpty = [list for list in values if list]
    #grabs the first value from each list that was added to check for empty
    newList = [n[0] for n in checkForEmpty]
    return newList

# Part 2

from data import Point
def x_coordinates(points:list[Point])->list[float]:
    xCoor = []
    #for each list in the list it takes the x coordinate from the list and adds it to xCor
    for points in points:
        xCoor.append(points.x)
    return xCoor

# Part 3

def are_in_positive_quadrant(points:list[Point])->list[float]:
    positive_points = []
    #for each list of two values in list, takes both values and adds them to positive points if
    #both the x cor and y cor are positive. Then returns the new list of positive coordinates
    for point in points:
        if point.x > 0 and point.y > 0:
            positive_points.append([point.x,point.y])
    return positive_points

# Part 4
def distance(first:Point, second:Point)-> float:
    #subtracts the absolute value of second x and first x and squares them. Does the same for the y value
    #once both have been subtracted, adds them up together and then square roots them
    return math.sqrt(abs(((second.x - first.x)**2)) + abs(((second.y - second.y)**2)))


# Part 5
def manhattan_distance(first:Point, second:Point)-> float:
    #absolute value of x1 and x2 added onto y1 and y 2
    return (abs(first.x - second.x) + abs(first.y - second.y))

# Part 6

def distance_all(points:list[Point])-> list[float]:
    result = []
    for i in range(len(points)):
        result.append(math.sqrt((points[i].x**2) + (points[i].y**2)))
    return result






