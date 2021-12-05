from math import sqrt, pow
from typing import List

class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
    
    def __eq__(self, __o: object) -> bool:
        return (self.x == __o.x and self.y == __o.y)
    
    def __hash__(self):
        return hash(self.x) ^ hash(self.y)
    
    def __str__(self) -> str:
        return f'Point({self.x}, {self.y})'

class Line:
    def __init__(self, p1: Point, p2: Point) -> None:
        self.p1 = p1
        self.p2 = p2
        
    def __str__(self):
        return f'({self.p1} -> {self.p2})'
        
    @property
    def x1(self):
        return self.p1.x
    
    @property
    def x2(self):
        return self.p2.x
    
    @property
    def y1(self):
        return self.p1.y
    
    @property
    def y2(self):
        return self.p2.y
    
    def is_horizontal_or_vertical(self):
        return self._is_horizontal() or self._is_vertical()
    
    def is_part2(self):
        return self.is_horizontal_or_vertical() or self._is_45_degree()
    
    def _is_horizontal(self):
        return self.y1 == self.y2
    
    def _is_vertical(self):
        return self.x1 == self.x2
    
    def _is_45_degree(self):
        return abs((self.y2 - self.y1)/(self.x2 - self.x1)) == 1
    
    def _get_distance(self):
        return sqrt(pow(self.x2 - self.x1, 2) + pow(self.y2 - self.y1, 2))
    
    def get_covered_points(self):
        min_y = min([self.y1, self.y2])
        max_y = max([self.y1, self.y2])
        min_x = min([self.x1, self.x2])
        max_x = max([self.x1, self.x2])
        if self._is_vertical():
            return [Point(self.x1, y) for y in range(min_y, max_y+1)]
        elif self._is_horizontal():
            return [Point(x, self.y1) for x in range(min_x, max_x+1)]
        elif self._is_45_degree():
            points = []
            raising_x = True if self.x2 > self.x1 else False
            raising_y = True if self.y2 > self.y1 else False
            for i in range(max_x - min_x + 1):
                if raising_x and raising_y:
                    points.append(Point(self.x1 + i, self.y1 + i))
                elif raising_x and not raising_y:
                    points.append(Point(self.x1 + i, self.y1 - i))
                elif not raising_x and raising_y:
                    points.append(Point(self.x1 - i, self.y1 + i))
                else:
                    points.append(Point(self.x1 - i, self.y1 - i))
            return points
            
        else: return []
            
    

def get_all_lines(file) -> List[Line]:
    with open('input5.txt', 'r') as file:
        lines = []
        for line in file:
            split = line.split('->')
            p1_data = list(map(lambda x: int(x), split[0].split(',')))
            p2_data = list(map(lambda x: int(x), split[1].split(',')))
            lines.append(Line(Point(*p1_data), Point(*p2_data)))
        return lines
    
def calculate_answer(array):
    overlap_points = dict()
    for line in array:
        covered_points = line.get_covered_points()
        for point in covered_points:
            if point in overlap_points:
                overlap_points[point] += 1
            else:
                overlap_points[point] = 1
    count = len(list(filter(lambda x: x>1, overlap_points.values())))
    return count


def part1():
    with open('input5.txt', 'r') as file:
        all_lines = get_all_lines(file)
        lines = list(filter(lambda line: line.is_horizontal_or_vertical(), all_lines))
        count = calculate_answer(lines)
        print(f'part 1 answer: {count}')


def part2():
    with open('input5.txt', 'r') as file:
        all_lines = get_all_lines(file)
        lines = list(filter(lambda line: line.is_part2(), all_lines))
        count = calculate_answer(lines)
        print(f'part 2 answer: {count}') 


def main():
    # part1()
    part2()


if __name__ == '__main__':
    main()
    