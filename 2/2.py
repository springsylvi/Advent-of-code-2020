import re

def part1(lines):
    valid = 0
    for line in lines:
        # parse line & extract values
        match = re.match("(.+)-(.+) (.): (.+)", line)
        groups = match.group(1,2,3,4)
        minC = int(groups[0])
        maxC = int(groups[1])
        char, pw = groups[2:]
        # count amount of char
        count = len("".join(map(lambda c : c if c == char else "", pw)))
        if count >= minC and count <= maxC:
            valid += 1
    return valid


def part2(lines):
    valid = 0
    for line in lines:
        # parse line & extract values
        match = re.match("(.+)-(.+) (.): (.+)", line)
        groups = match.group(1,2,3,4)
        pos1 = int(groups[0]) - 1
        pos2 = int(groups[1]) - 1
        char, pw = groups[2:]
        # check positions for char
        if (pw[pos1] == char) != (pw[pos2] == char):
            valid += 1
    return valid


with open("input2") as f:
    lines = f.readlines()
    print(part1(lines))
    print(part2(lines))
