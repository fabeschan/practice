

import random

def create_matrix(m, n):
    matrix = []
    for i in range(m):
        matrix.append([ random.choice([0, 1]) for j in range(n) ])
    return matrix

def create_puzzle(m=10, n=15):
    matrix = create_matrix(m, n)
    start = (random.choice(range(m)), random.choice(range(n)))
    goal = (random.choice(range(m)), random.choice(range(n)))
    matrix[start[0]][start[1]] = 1
    matrix[goal[0]][goal[1]] = 1
    return matrix, start, goal

def display_matrix(matrix, start, goal):
    # start or goal is a 2-tuple
    print "matrix"
    m = len(matrix)
    for i in range(m):
        row = matrix[i][:] # make copy
        if start[0] == i:
            row[start[1]] = 3
        if goal[0] == i:
            row[goal[1]] = 7
        print row

def bfs(matrix, start, goal):
    queue = [start]
    visited = set()

    while queue:
        # pick first one out
        # check if goal
        if queue[0] == goal:
            return True
        # if not goal, expand and add successors to back
        else:
            loc = queue[0]
            visited.add(loc)
            for s in successors(matrix, loc):
                if s not in visited:
                    queue.append(s)
            queue = queue[1:]
    return False


def successors(matrix, loc):
    s = []
    if loc[0]+1 < len(matrix):
        s.append((loc[0]+1, loc[1]))
    if loc[1]+1 < len(matrix[0]):
        s.append((loc[0], loc[1]+1))
    if loc[0]-1 >= 0:
        s.append((loc[0]-1, loc[1]))
    if loc[1]-1 >= 0:
        s.append((loc[0], loc[1]-1))
    return [ (x, y) for x, y in s if matrix[x][y] ]


if __name__ == '__main__':
    matrix, start, goal = create_puzzle()
    display_matrix(matrix, start, goal)
    print bfs(matrix, start, goal)

