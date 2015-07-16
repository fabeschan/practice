class node:
    self.children = [...]

def defrag(root):
    if not root:
        return
    i, j = 0, len(root.children)-1
    while i < len(root.children):
        if root.children[i]:
            defrag(root.children[i])
            i += 1
        else:
            del root.children[i]
            root.children.append(None)


