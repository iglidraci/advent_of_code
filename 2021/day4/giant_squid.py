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
    unmarked = 0
    for row in matrix:
        unmarked += sum(list(map(lambda x: int(x), filter(lambda x: x is not None, row))))
    return unmarked * number


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
    