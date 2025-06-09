from PriorityQueue import PriorityQueue

import math
(ox, oy) = (5, 4)
def dist(x, y):
    (dx, dy) = (ox-x, oy-y)
    return math.sqrt(dx*dx + dy*dy)

def isValidPos(x, y):
    if 0 <= x < MAZE_SIZE and 0 <= y < MAZE_SIZE:
        if map[y][x] == '0' or map[y][x] == 'x':
            return True
    return False

map = [ [ '1', '1', '1', '1', '1', '1' ],
        [ 'e', '0', '1', '0', '0', '1' ],
        [ '1', '0', '0', '0', '1', '1' ],
        [ '1', '0', '1', '0', '1', '1' ],
        [ '1', '0', '1', '0', '0', 'x' ],
        [ '1', '1', '1', '1', '1', '1' ]]
MAZE_SIZE = 6

def MySmartSearch():
    q = PriorityQueue()
    q.enqueue((0, 2, -dist(0, 1)))
    print('PQueue: ')

    while not q.isEmpty():
        here = q.dequeue()
        print(here[0:2], end='->')
        x, y, _ = here
        if (map[y][x] == 'x') : return True
        else:
            map[y][x] = '.'
            if isValidPos(x, y - 1) : q.enqueue((x, y - 1, -dist(x, y - 1)))
            if isValidPos(x, y + 1) : q.enqueue((x, y + 1, -dist(x, y + 1)))
            if isValidPos(x - 1, y) : q.enqueue((x - 1, y, -dist(x - 1, y)))
            if isValidPos(x + 1, y) : q.enqueue((x + 1, y, -dist(x + 1, y)))
        print('Priority Queue: ', q)
    return False

result = MySmartSearch()
if result : print(' --> Maze Solved!')
else : print(' --> No Solution!')
