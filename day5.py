file = open('input.txt', 'r')
highest_id = 0
"""
2^7 = 128
"""

# for line in file:
#     rows = (0, 127)
#     seats = (0, 7)
#     row = None
#     seat = None
#     for index in range(6):
#         if line[index] == 'F':
#             rows = (rows[0],rows[1] - (rows[1]-rows[0])//2 - 1)
#         else:
#             rows = (rows[0] + (rows[1]-rows[0])//2 + 1, rows[1])
#     if line[6] == "F":
#         row = rows[0]
#     else:
#         row = rows[1]        
#     print(f'row is {row}')
#     for index in range(7,9,1):
#         if line[index] == "L":
#             seats = (seats[0],seats[1] - (seats[1]-seats[0])//2 - 1)
#         else:
#             seats = (seats[0] + (seats[1]-seats[0])//2 + 1, seats[1])
#     if line[9] == 'L':
#         seat = seats[0]
#     else:
#         seat = seats[1]
#     calc = row*8 + seat
#     if calc > highest_id:
#         highest_id = calc    
        
# print(f'highest id is {highest_id}')

id_map = set()
for line in file:
    if line[0] != 'F' and line[6] != 'B':
        rows = (0, 127)
        seats = (0, 7)
        row = None
        seat = None
        for index in range(6):
            if line[index] == 'F':
                rows = (rows[0],rows[1] - (rows[1]-rows[0])//2 - 1)
            else:
                rows = (rows[0] + (rows[1]-rows[0])//2 + 1, rows[1])
        if line[6] == "F":
            row = rows[0]
        else:
            row = rows[1]        
        for index in range(7,9,1):
            if line[index] == "L":
                seats = (seats[0],seats[1] - (seats[1]-seats[0])//2 - 1)
            else:
                seats = (seats[0] + (seats[1]-seats[0])//2 + 1, seats[1])
        if line[9] == 'L':
            seat = seats[0]
        else:
            seat = seats[1]
        calc = row*8 + seat
        id_map.add(calc)
        if (calc-1) in id_map and (calc+1) in id_map:
            print(f'id {calc}')
print('done')        