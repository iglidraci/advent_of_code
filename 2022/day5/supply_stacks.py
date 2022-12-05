def read_input():
    with open('input', 'r') as file:
        for row in file:
            yield row.strip('\n')


def get_stacks(total_rows=8, total_stacks=9):
    stacks = [[] for _ in range(total_stacks)]
    counter = 0
    for row in read_input():
        i = 0
        j = 1
        while j < len(row):
            if crate := row[j]:
                stacks[i].append(crate)
            j += 4
            i += 1
        counter += 1
        if counter == total_rows:
            break
    return list(map(lambda x: list(filter(lambda y: y != ' ', x)), stacks))


def part1():
    stacks = get_stacks()
    for row in read_input():
        if row.startswith("move"):
            _, total, _, from_stack, _, to_stack = row.split(' ')
            for _ in range(int(total)):
                stacks[int(to_stack) - 1].insert(0, stacks[int(from_stack) - 1].pop(0))
    return "".join(map(lambda x: x[0], stacks))


if __name__ == '__main__':
    print(part1())
