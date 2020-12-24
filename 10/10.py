def part1(lines):
    jolts = [0] + lines + [lines[-1] + 3]
    diffs = [0,0,0]
    for i in range(len(jolts) - 1):
        d = jolts[i+1] - jolts[i]
        diffs[d-1] += 1
    return diffs[0] * diffs[2]


def paths_from(jolts, cache, i):
    n = jolts[i]
    if n in cache:
        return cache[n]
    else:
        paths = 0
        for j in range(i+1, i+4):
            if j == len(jolts):
                paths = 1
                break
            if jolts[j] <= n + 3:
                paths += paths_from(jolts, cache, j)
        cache[n] = paths
        return paths

def part2(lines):
    jolts = [0] + lines + [lines[-1] + 3]
    return paths_from(jolts, {}, 0)


with open("input10") as f:
    lines = sorted([int(x) for x in f.readlines()])
    print(part1(lines))
    print(part2(lines))
