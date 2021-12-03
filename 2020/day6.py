file = open('day6-input.txt', 'r')
group_answers = {}
total = 0
group_length = 0
for line in file:
    if line == '\n':
        for k in group_answers:
            if group_answers[k] == group_length:
                total += 1
        group_answers.clear()
        group_length = 0
    else:
        group_length += 1
        for char in line.strip():
            if char in group_answers:
                group_answers[char] += 1
            else:
                group_answers[char] = 1
                
for k in group_answers:
    if group_answers[k] == group_length:
        total += 1
print(f'total is {total}')
    