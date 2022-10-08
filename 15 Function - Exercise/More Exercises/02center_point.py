import sys
from math import floor, sqrt


def dist_calc(first, second):
    calculated_distance = (abs(first) ** 2) + (abs(second) ** 2)
    return sqrt(calculated_distance)


distance = sys.maxsize
points = ()

for point in range(2):
    x = float(input())
    y = float(input())
    check = dist_calc(x, y)
    if distance > check:
        distance = check
        points = (floor(x), floor(y))

print(points)




#################################### TASK CONDITION ############################
"""
                      2.	Center Point
You will be given the coordinates of two points on a Cartesian 
coordinate system - X1, Y1, X2, and Y2 on separate lines.
Write a function that prints the point which is closest to the 
center of the coordinate system (0, 0) in the format: "({X}, {Y})"
If the points are at the same distance from the center, print only the first one.
The resulting coordinates must be formatted to the lower integer.


____________________________________________________________________________________________
Example_01

Input
2
4
-1
2

Output
(-1, 2)


____________________________________________________________________________________________
Example_02

Input
10
14.5
-17.2
16

Output
(10, 14)

"""
