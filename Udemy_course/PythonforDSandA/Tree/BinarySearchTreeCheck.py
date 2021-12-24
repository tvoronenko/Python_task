import math


class Node:
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None

def is_valid_BST(root):
    return valid(root,-math.inf, math.inf)

def valid(node,min,max):
    if node is None:
        return True
    if (min<=node.value<= max):
        return  valid(node.left,min,node.value) and valid(node.right,node.value,max)
    return False


root= Node(10)
root.left = Node(5)
root.right= Node(30)

print(is_valid_BST(root)) # prints True, since this tree is valid

root = Node(10)
root.right = Node(20)
root.left = Node(5)
root.left.right = Node(15)

print(is_valid_BST(root)) # prints False, since 15 is to the left of 10