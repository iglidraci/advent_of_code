def part1():
    with open('input3.txt', 'r') as file:
        ones = [0 for _ in range(12)]
        zeros = [0 for _ in range(12)]
        gamma = ''
        epsilon = ''
        for line in file:
            for i, char in enumerate(line[:-1]):
                if char == '1':
                    ones[i] += 1
                else:
                    zeros[i] += 1
        for i in range(12):
            if ones[i] > zeros[i]:
                gamma += '1'
                epsilon += '0'
            else:
                gamma += '0'
                epsilon += '1'
        power = int(gamma, 2) * int(epsilon, 2)
        print(f'part 1 answer: {power}')


def part2():
    pass        
        

def main():
    part1()
    part2()

if __name__ == '__main__':
    main()
    