def get_pair(l, value):
        for i in range(len(l)):
            for v in l[i:]:
                if l[i] + v == value:
                    return True
        return False
    

def part1(lines):
    for i in range(25, len(lines)):
        prev = lines[i-25:i]
        value = lines[i]
        if not get_pair(prev, value):
            return value


def part2(lines, value):
    for i in range(len(lines)):
        total = 0
        j = i
        while total < value:
            total += lines[j]
            j += 1
        if total == value:
            # add largest and smallest
            big = lines[i]
            small = lines[i]
            for k in range(i+1,j):
                n = lines[k]
                if n > big:
                    big = n
                if n < small:
                    small = n
            return big + small


with open("input9") as f:
    lines = [int(x) for x in f.readlines()]
    value = part1(lines)
    print(value)
    print(part2(lines, value))
