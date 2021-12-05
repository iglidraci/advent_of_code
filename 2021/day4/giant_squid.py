'''
--- Day 4: Giant Squid ---
You're already almost 1.5km (almost a mile) below the 
surface of the ocean,already so deep that you can't see 
any sunlight. What you can see, however, is a giant squid 
that has attached itself to the outside of your submarine.

Maybe it wants to play bingo?

Bingo is played on a set of boards each consisting of a 5x5 grid of numbers. Numbers are chosen at random, and the chosen number is marked on all boards on which it appears. (Numbers may not appear on all boards.) If all numbers in any row or any column of a board are marked, that board wins. (Diagonals don't count.)

The submarine has a bingo subsystem to help passengers (currently, you and the giant squid) pass the time. It automatically generates a random order in which to draw numbers and a random set of boards (your puzzle input). For example:
'''


def check_input(matrices):
    for matrix in matrices:
        assert len(matrix) == 5
        for array in matrix:
            assert len(array) == 5
            

def mark_matrices(matrices, number):
    '''turn all the locations of number into None'''
    return [
                [
                    [x if x!= number else None for x in row]    
                    for row in matrix
                ]
                for matrix in matrices
            ]
    
def column_from_matrix(matrix, i):
    '''return the column of a matrix'''
    return [row[i] for row in matrix]    


def is_winner(matrix):
    for row in matrix:
        if not any(row):
            return True
    for i in range(5):
        col_i = column_from_matrix(matrix, i)
        if not any(col_i):
            return True
    return False


def get_if_winner(matrices):
    '''return the winning matrix if there is one else None'''
    for matrix in matrices:
        if is_winner(matrix):
            return matrix
    return None

def get_winners(matrices):
    """get all the winners of current round"""
    return list(filter(is_winner, matrices))


def calculate_points(matrix, number):
    '''
    make the matrix flat first
    filter all non None elements
    map them into integers
    sum them and multiply by the given number
    '''
    return number * sum(map(lambda x: int(x),
                            filter(lambda x: x,
                                   (y for x in matrix for y in x))))


def build_matrices_from_file(file):
    matrices = []
    matrix = []
    for line in file:
        if line == '\n':
            matrices.append(matrix)
            matrix = []
        else:
            matrix.append(list(filter(lambda x: x != '', line[:-1].split(' '))))
    matrices.append(matrix)
    return matrices

def part1():
    with open('input4.txt', 'r') as file:
        numbers = next(file).split(',')
        next(file)
        matrices = build_matrices_from_file(file)
        # check_input(matrices)
        
        for number in numbers:
            matrices = mark_matrices(matrices, number)
            winner = get_if_winner(matrices)
            if winner:
                points = calculate_points(winner, int(number))
                print(f'part 1 answer: {points}')
                break

def part2():
    with open('input4.txt', 'r') as file:
        numbers = next(file)[:-1].split(',')
        next(file)
        matrices = build_matrices_from_file(file)
        winners = []
        last_numbers = []
        for number in numbers:
            if not matrices:
                break
            matrices = mark_matrices(matrices, number)
            winner = get_winners(matrices)
            if winner:
                for w in winner:
                    matrices.remove(w)
                winners.extend(winner)
                last_numbers.append(int(number))
        points = calculate_points(winners[-1], last_numbers[-1])
        print(f'part 2: {points}')

def main():
    part1()
    part2()


if __name__ == '__main__':
    main()
    