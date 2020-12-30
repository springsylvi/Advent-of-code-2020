def part1(time, buses):
    min_wait = time
    bus_id = None
    for bus in buses:
        if bus == "x":
            continue
        wait = bus - (time % bus)
        if wait < min_wait:
            min_wait = wait
            bus_id = bus
    return min_wait * bus_id


def part2(buses):
    x = buses[0]
    y = 1
    for i in range(len(buses)):
        bus = buses[i]
        if bus == "x":
            continue
        while (x % bus != (bus - i) % bus):
            x += y
        y *= bus
    return x


with open("input13") as f:
    lines = f.readlines()
    time = int(lines[0])
    buses = [x if x == "x" else int(x) for x in lines[1].split(",")]
    print(part1(time, buses))
    print(part2(buses))
