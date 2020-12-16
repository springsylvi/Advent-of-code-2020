def part1(lines):
    for i,line in lines:
        remainder = 2020 - line
        for j,line2 in lines[i+1:]:
            if line2 == remainder:
                return(line*line2)

def part2(lines):
    for i,line in lines:
        remainder = 2020 - line
        for j,line2 in lines[i+1:]:
            for k,line3 in lines[j+1:]:
                if line2 + line3 == remainder:
                    return(line*line2*line3)

with open("input1") as f:
    lines = list(enumerate(map(int, f.readlines())))
    print(part1(lines))
    print(part2(lines))
