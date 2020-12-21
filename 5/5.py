def part1(lines):
    big = 0
    for line in lines:
        row = int(line[:7].replace("F", "0").replace("B", "1"), base=2)
        col = int(line[7:].replace("L", "0").replace("R", "1"), base=2)
        ID = row*8 + col
        if ID > big:
            big = ID
    return big


def part2(lines):
    IDs = []
    for line in lines:
        row = int(line[:7].replace("F", "0").replace("B", "1"), base=2)
        col = int(line[7:].replace("L", "0").replace("R", "1"), base=2)
        IDs.append(row*8 + col)
    IDs.sort()
    for i in range(len(IDs)-1):
        if IDs[i] + 1 != IDs[i + 1]:
            return IDs[i] + 1

with open("input5") as f:
    lines = f.readlines()
    print(part1(lines))
    print(part2(lines))
