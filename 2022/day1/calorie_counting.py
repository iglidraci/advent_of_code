def part1():
    with open('input.txt') as file:
        max_calorie = 0
        current = 0
        for row in file:
            calorie = row.strip('\n')
            if calorie:
                current += int(row)
            else:
                if current > max_calorie:
                    max_calorie = current
                current = 0
        return max_calorie


def part2():
    with open('input.txt') as file:
        calories = []
        current = 0
        for row in file:
            calorie = row.strip('\n')
            if calorie:
                current += int(calorie)
            else:
                calories.append(current)
                current = 0
        return sum(sorted(calories, reverse=True)[:3])


if __name__ == '__main__':
    print(part1())
    print(part2())
