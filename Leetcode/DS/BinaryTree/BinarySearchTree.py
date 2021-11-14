from collections import deque
from Leetcode.DS.BinaryTree.BinaryTreeNode import BinaryTreeNode


class BinarySearchTree():
    """def __init__(self,arr):
        self.root = None

        def helper(left, right):
            if left > right:
                return None

            p = left + (right - left) // 2

            root = BinaryTreeNode(arr[p])
            root.left = helper(left, p - 1)
            root.right = helper(p + 1, right)
            return root

        self.root =  helper(0, len(arr) - 1)

    def insert(self,node,d):
        pNew = BinaryTreeNode(d)
        if node == None:
            return pNew

        parent = None
        pTemp = node
        while (pTemp != None):
            parent = pTemp
            if d < pTemp.data:
                pTemp = pTemp.left
            else:
                pTemp = pTemp.right

        if d < parent.data:
            parent.left = pNew
        else:
            parent.right = pNew

        return node

    def __str__(self):
        output = ""

        if self.root is None:
            return

        q = deque()
        q.append(self.root)
        while len(q) > 0:
            output += "\n"
            for _ in range(len(q)):
                r = q.pop()
                output += str(r.data) + " "
                if r.left:
                    q.append(r.left)
                if r.right:
                    q.append(r.right)

        return output
"""
    def __init__(self,arr):
        self.root = None

    def __str__(self):
        # level-by-level pretty-printer
        nodes = deque([self])
        answer = ''
        while len(nodes):
            node = nodes.popleft()
            if not node:
                continue
            answer += str(node.value)
            nodes.append(node.left)
            nodes.append(node.right)
        return answer

arr1 = [100,50,200,25,125,350]
arr1.sort()
arr2 = [1,2,10,50,180,199]
arr2.sort()
root1 = BinarySearchTree(arr1)
print(root1)
root2 = BinarySearchTree(arr2)

print(root2)