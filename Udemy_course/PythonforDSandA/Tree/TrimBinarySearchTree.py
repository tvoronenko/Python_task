from Udemy_course.PythonforDSandA.Tree.BinaryTree import BinaryTree
from Udemy_course.PythonforDSandA.Tree.TreeLevelOrderPrint import *

def trimBST(root, min_val, max_val):
    if root is None:
        return
    root.left = trimBST(root.left, min_val, max_val)
    root.right = trimBST(root.right, min_val, max_val)
    if min_val <= root.key <= max_val:
        return root
    if root.key < min_val:
        return root.right
    if root.key > max_val:
        return root.left


r = BinaryTree(8)
r.left = BinaryTree(3)
r.left.left = BinaryTree(1)
r.left.right = BinaryTree(6)
r.left.right.left = BinaryTree(4)
r.left.right.right = BinaryTree(7)
r.right = BinaryTree(10)
r.right.right = BinaryTree(14)
r.right.right.left = BinaryTree(13)
levelOrderPrint(r)
p=trimBST(r,5,13)
levelOrderPrint(p)