def part1(lines):
    total = 0
    answers = set()
    for line in lines:
        if line == "\n":
            # add group's answers to total
            total += len(answers)
            answers = set()
        else:
            # add person's answers to group
            for char in line.strip():
                answers.add(char)
    total += len(answers)
    return total


def part2(lines):
    total = 0
    answers = []
    for line in lines:
        if line == "\n":
            # add intersection of group's answers to total
            group = answers[0]
            for p in answers:
                group = group.intersection(p)
            total += len(group)
            answers = []
        else:
            # add person's answers to group
            person = set()
            for char in line.strip():
                person.add(char)
            answers.append(person)
    group = answers[0]
    for p in answers:
        group = group.intersection(p)
    total += len(group)
    return total
   

with open("input6") as f:
    lines = f.readlines()
    print(part1(lines))
    print(part2(lines))
