from math import *

def part1(lines):
    x,y,angle = 0,0,0
    for line in lines:
        t = line[0]
        v = int(line[1:])
        if t == "N":
            y += v
        elif t == "S":
            y -= v
        elif t == "E":
            x += v
        elif t == "W":
            x -= v
        elif t == "L":
            angle += v * pi / 180
        elif t == "R":
            angle -= v * pi / 180
        elif t == "F":
            x += v * round(cos(angle))
            y += v * round(sin(angle))
    return abs(x) + abs(y)


def part2(lines):
    x,y = 0,0
    wx,wy = 10,1
    for line in lines:
        t = line[0]
        v = int(line[1:])
        if t == "N":
            wy += v
        elif t == "S":
            wy -= v
        elif t == "E":
            wx += v
        elif t == "W":
            wx -= v
        elif t == "F":
            x += v * wx
            y += v * wy
        else:
            if t == "R":
                v = 360 - v
            if v == 180:
                wx,wy = -wx,-wy
            elif v == 90:
                wx,wy = -wy,wx
            else: # v == 270
                wx,wy = wy,-wx
    return abs(x) + abs(y)


with open("input12") as f:
    lines = f.readlines()
    print(part1(lines))
    print(part2(lines))

