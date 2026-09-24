#Write a python program to store two points as tuples and calculate the distance between them.
import math

point1 = (2, 3)
point2 = (6, 7)


distance = math.sqrt((point2[0] - point1[0])**2 +
                     (point2[1] - point1[1])**2)

print("Distance between the points:", distance)
