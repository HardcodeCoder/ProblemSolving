""" 
  @Author: hardcodecoder
  @Date:   06:16:26 Monday 06 July 2020
  @Last modified by:   hardcodecoder
  @Last modified time: 08:12:43 Friday 10 July 2020
"""

"""
Given N number of cars on a 2d plane with the (x, y) coordinate of each car and velocity with which
each car is approaching the origin (0, 0). Find the number of collisions

Note : - Calculate collisions only at origin. Ignore the other collisions. 
Assume that each car continues on its respective path even after the collision 
without change of direction or speed for an infinite distance.
"""

import math

# Number of cars
c = int(input())
dic = {}


for i in range(c):
    # Get the coordinates and velocity of each car
    x,y,v = map(int, input().split())

    #Calculate the time taken by the car to reach the origin
    t = math.sqrt(((x/v)**2 + (y/v)**2))

    
    if dic.get(t) == None:
        dic[t] = 1   # If time 't' does not exists in dict, set count to 1
    
    else:
        dic[t] = dic[t] + 1 # Ttime 't' exists in dict increase count by 1

collisions = 0

# Calculate all collisions
for entry in dic:
    if dic[entry] != 1:
        collisions = collisions + (dic[entry] * (dic[entry] - 1))/2

print(int(collisions))