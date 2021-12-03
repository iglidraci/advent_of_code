def part1():
    with open('input2.txt', 'r') as file:
        horizontal_pos = 0
        depth = 0
        for line in file:
            split = line.split(' ')
            if split[0] == 'forward':
                horizontal_pos += int(split[1])
            elif split[0] == 'down':
                depth += int(split[1])
            else:
                depth -= int(split[1])
        res = horizontal_pos * depth
        print(f'part 1 result: {res}')
        
def part2():
    with open('input2.txt', 'r') as file:
        horizontal_pos = 0
        depth = 0
        aim = 0
        for line in file:
            split = line.split(' ')
            if split[0] == 'forward':
                horizontal_pos += int(split[1])
                depth += aim * int(split[1])
            elif split[0] == 'down':
                aim += int(split[1])
            else:
                aim -= int(split[1])
        res = horizontal_pos * depth
        print(f'part 2 result: {res}')

def main():
    part1()
    part2()


if __name__ == '__main__':
    main()
    