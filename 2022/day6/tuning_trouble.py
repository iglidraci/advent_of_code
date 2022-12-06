def read_input():
    with open('input', 'r') as file:
        for row in file:
            yield row.strip('\n')


def distinct_chars(unique_chars):
    msg = next(read_input())
    seen = set()
    left, right = [0, 0]
    while right != len(msg):
        if (char := msg[right]) not in seen:
            seen.add(char)
            right += 1
        else:
            seen.remove(msg[left])
            left += 1
        if len(seen) == unique_chars:
            break
    return right


def part1():
    return distinct_chars(4)


def part2():
    return distinct_chars(14)


if __name__ == '__main__':
    print(part1())
    print(part2())
