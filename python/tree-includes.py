class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None
        
a = Node(1)
b = Node(6)
c = Node(0)
d = Node(3)
e = Node(-6)
f = Node(2)
g = Node(2)
h = Node(2)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
e.left = g
f.right = h

#      1
#    /   \
#   6     0
#  / \     \
# 3   -6    2
#    /       \
#   2         2

def tree_includes(root, val):
    # traverse depth first
    if root is None:
        return False
    stack = [ root ]
    while stack:
        curr = stack.pop()
        if curr.val == val:
            return True
        # print(curr.val)
        if curr.right is not None:
            stack.append(curr.right)
        if curr.left is not None:
            stack.append(curr.left)
    
    return False

# def depth_first_values(root):
#     # traverse depth first
#     if root is None:
#         return []
    
#     left_values = depth_first_values(root.left) # [ b, d, e ]
#     right_values = depth_first_values(root.right) # [ c, f ]
    
#     return [ root.val, *left_values, *right_values]
    


print(tree_sum(a)) # -> 10

