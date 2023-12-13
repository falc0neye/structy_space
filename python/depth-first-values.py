class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None
        
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

print(None)

def depth_first_values(root):
    # traverse depth first
    if root is None:
        return 0
    stack = [ root ]
    values = []
    while stack:
        curr = stack.pop()
        values.append(curr.val)
        print(curr.val)
        if curr.right is not None:
            stack.append(curr.right)
        if curr.left is not None:
            stack.append(curr.left)
    
    return values

# def depth_first_values(root):
#     # traverse depth first
#     if root is None:
#         return []
    
#     left_values = depth_first_values(root.left) # [ b, d, e ]
#     right_values = depth_first_values(root.right) # [ c, f ]
    
#     return [ root.val, *left_values, *right_values]
    


print(depth_first_values(a))
#   -> ['a', 'b', 'd', 'e', 'c', 'f']
