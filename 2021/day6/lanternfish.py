def decide_state(nr):
    if nr == 0: return 6
    else: return nr-1

def part1():
    with open('input6.txt', 'r') as file:
        numbers = list(map(lambda x: int(x), next(file).split(',')))
        days = 80
        for _ in range(days):
            new_numbers = []
            for i in range(len(numbers)):
                if numbers[i] == 0:
                    new_numbers.append(8)
                nr = decide_state(numbers[i])
                numbers[i] = nr
            numbers.extend(new_numbers)
        print(f'part 1 answer: {len(numbers)}')


def main():
    part1()


if __name__ == '__main__':
    main()
    