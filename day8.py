acc = 0
current_instruction = 0
visited_instructions = set()
while True:
    if current_instruction in visited_instructions:
        print(f'accumulator is {acc}')
        print(f'length is {len(visited_instructions)}')
        break
    else:
        file = open('day8-input.txt', 'r')
        for index, line in enumerate(file):
            if current_instruction < index:
                break
            elif index == current_instruction:
                visited_instructions.add(index)         
                lines = (line.strip()).split(' ')
                operation = lines[0]
                number = lines[1]
                if operation == 'acc':
                    acc += int(number)
                    current_instruction += 1
                elif operation == 'jmp':
                    current_instruction += int(number)
                else:
                    current_instruction += 1

    