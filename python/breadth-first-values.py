from collections import deque

class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None


def breadth_first_values(root):
    if root is None:
        return []
    # Traverse and add values using queue
    values = []
    q = deque( [ root ] )
    
    while q:
        curr = q.popleft()
        values.append(curr.val)
        # print(curr.val)
        if curr.left is not None:
            q.append(curr.left)
        if curr.right is not None:
            q.append(curr.right)
            
    return values

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#      a
#    /   \
#   b     c
#  / \     \
# d   e     f

print(breadth_first_values(a))
#    -> ['a', 'b', 'c', 'd', 'e', 'f']





