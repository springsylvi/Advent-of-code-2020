import re

def get_graph(lines):
    g = {}
    for line in lines:
        try:
            # parse line
            adj = []
            match = re.match("(.+) bags contain(.+)\n", line)
            bag = match.group(1)
            tail = match.group(2).split(",")
            for s in tail:
                match2 = re.match(" (.+?) (.+?) bags*", s)
                if not match2:
                    break
                # add edge to graph
                inner = match2.group(2)
                count = int(match2.group(1))
                adj.append((bag, inner, count))
                if inner not in g:
                    g[inner] = []
                g[inner].append((bag, inner, count))
            if bag not in g:
                g[bag] = []
            g[bag] += adj
        except:
            pass
    return g


def part1(g):
    bags = set()
    c = set()
    c.add("shiny gold")
    while len(c) > 0:
        bags.update(c)
        n = set()
        for bag in c:
            for t in g[bag]:
                if t[1] == bag:
                    n.add(t[0])
        c = n
    return len(bags) - 1


def part2(g):
    bags = 0
    c = {}
    c["shiny gold"] = 1
    while len(c) > 0:
        print(c)
        n = {}
        for bag,count in c.items():
            for t in g[bag]:
                if t[0] == bag:
                    n[t[1]] = count * t[2]
                    bags += count * t[2]
        c = n
    return bags


with open("input7") as f:
    lines = f.readlines()
    g = get_graph(lines)
    print(part1(g))
    print(part2(g))
