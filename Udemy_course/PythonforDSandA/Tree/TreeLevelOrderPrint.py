from collections import deque

from Udemy_course.PythonforDSandA.Tree.BinaryTree import BinaryTree


def levelOrderPrint(tree):
    if tree is None:
        return
    queue = deque()
    queue.append(tree)
    while queue:
        print("")
        for _ in range(len(queue)):
            cur = queue.popleft()
            print(cur.key,end=" ")
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)

if __name__ == '__main__':
    r = BinaryTree('8')
    r.left = BinaryTree('3')
    r.left.left = BinaryTree('1')
    r.left.right = BinaryTree('6')
    r.left.right.left = BinaryTree('4')
    r.left.right.right = BinaryTree('7')
    r.right = BinaryTree('10')
    r.right.right = BinaryTree('14')
    r.right.right.left = BinaryTree('13')

    levelOrderPrint(r)
#1
#2 3
# 4 5  6
