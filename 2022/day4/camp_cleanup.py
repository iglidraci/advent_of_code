def read_input():
    with open('input', 'r') as file:
        for row in file:
            yield row.strip('\n')


fully_contains = lambda x1, x2, y1, y2: (y1 >= x1 and y2 <= x2) or (x1 >= y1 and x2 <= y2)


def part1():
    count = 0
    for row in read_input():
        elf1, elf2 = row.split(',')
        x1, x2 = list(map(int, elf1.split('-')))
        y1, y2 = list(map(int, elf2.split('-')))
        if fully_contains(x1, x2, y1, y2):
            count += 1
    return count


def part2():
    count = 0
    for row in read_input():
        elf1, elf2 = row.split(',')
        x1, x2 = list(map(int, elf1.split('-')))
        y1, y2 = list(map(int, elf2.split('-')))
        section1 = set()
        section2 = set()
        for i in range(x1, x2 + 1):
            section1.add(i)
        for i in range(y1, y2 + 1):
            section2.add(i)
        intersect = section1.intersection(section2)
        if intersect:
            count += 1
    return count


if __name__ == '__main__':
    print(part1())
    print(part2())