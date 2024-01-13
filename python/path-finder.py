# Write a function, path_finder, that takes in the root of a binary tree and a target value. 
# The function should return an array representing a path to the target value. 
# If the target value is not found in the tree, then return None.
# You may assume that the tree contains unique values.


class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")

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

def path_finder(root, value):
    if root is None:
        return None
    
    if root.val == value:
        return [root.val]
    
    left_values = path_finder(root.left, value)
    right_values = path_finder(root.right, value)
    
    if left_values is not None:
        return [root.val] + left_values
    
    if right_values is not None:
        return [root.val] + right_values
    
    return None



# path_finder(a, 'e') # -> [ 'a', 'b', 'e' ]