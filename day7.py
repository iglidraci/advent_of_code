class DirectedGraph:
    def __init__(self):
        self.adjacency_list = {}

    def add_node(self, val):
        if val not in self.adjacency_list:
            self.adjacency_list[val] = set()

    def add_edge(self, from_node, to_node):
        if to_node not in self.adjacency_list:
            self.add_node(to_node)
        if from_node in self.adjacency_list:
            self.adjacency_list[from_node].add(to_node)
        else:
            self.adjacency_list[from_node] = set()
            self.adjacency_list[from_node].add(to_node)


graph = DirectedGraph()

file = open('day7-input.txt', 'r')
count = 0
already_counted = set()
for line in file:
    if line.split(' ')[0] != 'shiny':
        all_bags = ((line.strip()).split('contain')[1]).split(',')
        for bag in all_bags:
            splited_line = (bag.strip()).split(' ')
            try:
                nr = int(splited_line[0])
                if splited_line[1]=='shiny' and splited_line[2]=='gold':
                    count += 1
            except ValueError as identifier:
                print('no number found')
                
print(f'count is {count}')


