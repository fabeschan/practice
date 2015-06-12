
import random

class Node(object):

    def __init__(self, left=None, right=None, data=None):
        self.left = left
        self.right = right
        self.data = data

def bfs(root):
    queue = [root]
    while queue:
        # expand and visit front, put children at back
        front = queue[0]
        if front:
            print front.data
            queue = queue[1:] + [front.left, front.right]
        else:
            queue = queue[1:]

def bfs_zigzag(root):
    pass

def dfs(root, level=0):
    if root:
        root.data = level
        dfs(root.left, level+1)
        dfs(root.right, level+1)

def generate_tree():
    max_level = 7
    root = Node()
    q1 = [root]
    for i in range(max_level):
        q = q1
        q1 = []
        for n in q:
            if random.choice([0, 1]):
                n.left = Node()
                q1.append(n.left)
            if random.choice([0, 1]):
                n.right = Node()
                q1.append(n.right)
    return root

if __name__ == '__main__':
    root = generate_tree()
    dfs(root) # label the levels
    bfs(root)
