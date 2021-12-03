def larger_than_previous_measurements(array):
    prev1 = None
    prev2 = None
    increased = 0
    for i, line in enumerate(array):
        if i != 0:
            prev1 = prev2
        prev2 = line
        if prev1 and (int(prev2) > int(prev1)):
            increased += 1
    return increased


def part1():
    with open('input1.txt', 'r') as file:
        increased = larger_than_previous_measurements(file)
        print(increased)
        
def part2():
    '''
    Your goal now is to count the number of times the sum of measurements in this sliding window 
    increases from the previous sum
    '''
    with open('input1.txt', 'r') as file:
        file = list(file)
        three_sums = []
        current_index = 0
        while True:
            three_elements = file[current_index : current_index+3]
            if len(three_elements) != 3 :
                break
            three_sums.append(sum(map(lambda x: int(x), three_elements)))
            current_index += 1
        increases = larger_than_previous_measurements(three_sums)
        print(increases)


if __name__ == '__main__':
    part2()
    