#!/usr/bin/env python
import math


def solve(p, x, y):
    r = 50
    theta = math.pi/2 - math.asin((y-50)/r)
    print(theta)
    arc_angle = p/100 * 2 * math.pi
    if theta > 0:
        if y < 50 and y > 0:
            theta += math.pi/2
    elif theta < 0:
        if y > 0 and y < 50:
            theta = math.pi - theta
        else:
            theta = 1.5 * math.pi -theta
    if theta <= arc_angle:
        print(theta, arc_angle)
        return "black"
    else:
        print(theta, arc_angle)
        return "white"

t = int(input())

for i in range(1, t+1):
    p, x, y = [int(s) for s in input().split(" ")]
    print("case #{}: {}".format(i, solve(p,x,y)))
