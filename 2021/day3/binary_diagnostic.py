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
        
        
def get_ones_and_zeros(array, position) -> tuple:
    '''return the number of ones and zeros in each
    element of the array at given postion
    return ones, zeros as a tuple
    '''
    ones = 0
    zeros = 0
    for x in array:
        if x[position] == '1':
            ones += 1
        else:
            zeros += 1
    return ones, zeros


def part2():
    with open('input3.txt', 'r') as file:
        o2 = list(file)
        co2  = o2.copy()
        index = 0
        while True:
            if len(o2) == 1:
                break
            ones, zeros = get_ones_and_zeros(o2, index%12)
            char = '1' if ones >= zeros else '0'
            o2 = list(filter(lambda s: s[index%12]==char, o2))
            index += 1
        index = 0
        while True:
            if len(co2) == 1:
                break
            ones, zeros = get_ones_and_zeros(co2, index%12)
            char = '0' if zeros <= ones else '1'
            co2 = list(filter(lambda s: s[index%12]==char, co2))
            index += 1
        life_support_rate = int(co2[0], 2) * int(o2[0], 2)
        print(f'part 2 answer: {life_support_rate}')

def main():
    part1()
    part2()

if __name__ == '__main__':
    main()
    