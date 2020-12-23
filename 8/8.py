import re

def part1(lines):
    acc = 0
    pc = 0
    repeat = set()
    while True:
        if pc in repeat:
            return acc
        line = lines[pc]
        repeat.add(pc)
        match = re.match("(acc|jmp|nop) ([-+].+)\n", line)
        op = match.group(1)
        if op == "acc":
            acc += int(match.group(2))
            pc += 1
        elif op == "jmp":
            pc += int(match.group(2))
        else:
            pc += 1


def part2(lines):

    for corrupt in range(len(lines)):
        cline = lines[corrupt]
        match0 = re.match("(acc|jmp|nop) ([-+].+)\n", cline)
        op = match0.group(1)
        if op == "acc":
            continue
        elif op == "jmp":
            lines[corrupt] = "nop" + cline[3:]
        else:
            lines[corrupt] = "jmp" + cline[3:]

        acc = 0
        pc = 0
        repeat = set()
        while True:
            if pc == len(lines):
                return acc
            if pc in repeat:
                lines[corrupt] = cline
                break
            line = lines[pc]
            repeat.add(pc)
            match = re.match("(acc|jmp|nop) ([-+].+)\n", line)
            op = match.group(1)
            if op == "acc":
                acc += int(match.group(2))
                pc += 1
            elif op == "jmp":
                pc += int(match.group(2))
            else:
                pc += 1


with open("input8") as f:
    lines = f.readlines()
    print(part1(lines))
    print(part2(lines))
