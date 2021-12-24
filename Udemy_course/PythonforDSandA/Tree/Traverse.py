from Udemy_course.PythonforDSandA.Tree.BinaryTree import BinaryTree
from Udemy_course.PythonforDSandA.Tree.TreeLevelOrderPrint import *

def preorder_rec(root):
    if root is None:
        return
    print(root.key, end=" ")
    preorder_rec(root.left)
    preorder_rec(root.right)

def preorder(root):
    if root is None:
        return

    stack = [root]
    while stack:
        cur = stack.pop()
        print(cur.key, end=" ")
        if cur.right:
            stack.append(cur.right)
        if cur.left:
            stack.append(cur.left)


def inorder_rec(root):
    if root is None:
        return
    inorder_rec(root.left)
    print(root.key, end=" ")
    inorder_rec(root.right)

def inorder(root):
    if root is None:
        return

    stack = deque()
    cur = root
    while cur or stack:
        while cur:
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()
        print(cur.key, end=" ")
        cur = cur.right


def postorder_rec(root):
    if root is None:
        return
    postorder_rec(root.left)
    postorder_rec(root.right)
    print(root.key, end=" ")

def postorder(root):
    if root is None:
        return

    stack = [(root,False)]
    while stack:
        cur,visited = stack.pop()
        if visited:
            print(cur.key, end=" ")
        else:
            stack.append((cur, True))
            if cur.right:
                stack.append((cur.right,False))
            if cur.left:
                stack.append((cur.left,False))

r = BinaryTree(8)
r.left = BinaryTree(3)
r.left.left = BinaryTree(1)
r.left.right = BinaryTree(6)
r.left.right.left = BinaryTree(4)
r.left.right.right = BinaryTree(7)
r.right = BinaryTree(10)
r.right.right = BinaryTree(14)
r.right.right.left = BinaryTree(13)
print("level")
levelOrderPrint(r)
print("\npreorder rec")
preorder_rec(r)
print("\npreorder")
preorder(r)
print("\ninorder_rec")
inorder_rec(r)
print("\ninorder")
inorder(r)
print("\npostorder_rec")
postorder_rec(r)
print("\npostorder")
postorder(r)