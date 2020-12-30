import re


def get_grid(lines):
    g = {}
    for i in range(len(lines)):
        line = lines[i]
        for j in range(len(line)):
            char = line[j]
            g[(j,i)] = char
    return g


def part1(g):
    adj = [(0,1),(0,-1),(-1,1),(-1,0),(-1,-1),(1,1),(1,0),(1,-1)]
    stable = False
    while not stable:
        stable = True
        update = {}
        for coords,char in g.items():
            if char == ".":
                continue
            x,y = coords
            count = 0
            for dx,dy in adj:
                if g.get((x+dx,y+dy)) == "#":
                    count += 1
            if char == "L" and count == 0:
                update[coords] = "#"
                stable = False
            if char == "#" and count >= 4:
                update[coords] = "L"
                stable = False
        g.update(update)
    return list(g.values()).count("#")

    
def part2(g):
    adj = [(0,1),(0,-1),(-1,1),(-1,0),(-1,-1),(1,1),(1,0),(1,-1)]
    stable = False
    while not stable:
        stable = True
        update = {}
        for coords,char in g.items():
            if char == ".":
                continue
            x,y = coords
            count = 0
            for dx,dy in adj:
                nx = x+dx
                ny = y+dy
                while g.get((nx,ny)) == ".":
                    nx += dx
                    ny += dy
                if g.get((nx,ny)) == "#":
                    count += 1
            if char == "L" and count == 0:
                update[coords] = "#"
                stable = False
            if char == "#" and count >= 5:
                update[coords] = "L"
                stable = False
        g.update(update)
    return list(g.values()).count("#")


with open("input11") as f:
    lines = [x.strip() for x in f.readlines()]
    g = get_grid(lines)
    #print(part1(g))
    print(part2(g))


