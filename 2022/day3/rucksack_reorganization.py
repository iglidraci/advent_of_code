def read_input():
    with open('input', 'r') as file:
        for row in file:
            yield row.strip('\n')


def get_priority(char):
    if 'a' <= char <= 'z':
        return ord(char) - ord('a') + 1
    else:
        return ord(char) - ord('A') + 27


def part1():
    priority = 0
    for rucksack in read_input():
        mid = int(len(rucksack)/2)
        first_compartment = rucksack[0:mid]
        second_compartment = rucksack[mid:]
        common = set()
        for char in first_compartment:
            if char in second_compartment:
                common.add(char)
        for char in common:
            priority += get_priority(char)
    return priority


def part2():
    i = 0
    priority = 0
    group = [set() for _ in range(3)]
    for elf in read_input():
        group[i] = set(elf)
        i = i + 1
        if i == 3:
            common = group[0].intersection(group[1]).intersection(group[2])
            priority += get_priority(common.pop())
            i = 0
    return priority


if __name__ == '__main__':
    print(part1())
    print(part2())

