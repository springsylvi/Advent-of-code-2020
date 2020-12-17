def part1(lines):
    x,y = 0,0
    trees = 0
    # trace path
    while (y + 1 < len(lines)):
        x += 3
        y += 1
        row = lines[y][:-1]
        # count trees
        if row[x % len(row)] == "#":
            trees += 1
    return trees


def part2(lines):
    product = 1
    for dx,dy in [(1,1),(3,1),(5,1),(7,1),(1,2)]:
        x,y = 0,0
        trees = 0
        while (y + dy < len(lines)):
            x += dx
            y += dy
            row = lines[y][:-1]
            if row[x % len(row)] == "#":
                trees += 1
        product *= trees
    return product


with open("input3") as f:
    lines = f.readlines()
    print(part1(lines))
    print(part2(lines))
