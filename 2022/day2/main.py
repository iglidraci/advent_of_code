ROCK = 'A'
PAPER = 'B'
SCISSOR = 'C'

LOSE = 'X'
DRAW = 'Y'
WIN = 'Z'


def read_input():
    with open('input') as file:
        for row in file:
            opp, you = row.strip('\n').split(' ')
            yield opp, you


def part1():
    score = 0
    for opp, you in read_input():
        if you == 'X': you = ROCK
        elif you == 'Y': you = PAPER
        elif you == 'Z': you = SCISSOR
        score += play(opp, you)
    return score


def part2():
    score = 0
    for opp, you in read_input():
        if you == LOSE:
            if opp == ROCK: you = SCISSOR
            elif opp == PAPER: you = ROCK
            elif opp == SCISSOR: you = PAPER
        elif you == DRAW:
            you = opp
        elif you == WIN:
            if opp == ROCK: you = PAPER
            elif opp == SCISSOR: you = ROCK
            elif opp == PAPER: you = SCISSOR
        score += play(opp, you)
    return score


def play(opp, you):
    score = 0
    if you == ROCK:
        score += 1
    elif you == PAPER:
        score += 2
    elif you == SCISSOR:
        score += 3
    if you == opp:
        score += 3
    elif (you == ROCK and opp == SCISSOR) or (you == SCISSOR and opp == PAPER) or (
            you == PAPER and opp == ROCK):
        score += 6
    return score


if __name__ == '__main__':
    '''
    12759 wrong
    '''
    print(part1())
    print(part2())
