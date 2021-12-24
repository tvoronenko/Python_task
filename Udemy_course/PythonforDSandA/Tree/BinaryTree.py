class BinaryTree():
    def __init__(self,value):
        self.key = value
        self.left = None
        self.right = None

    def insertLeft(self,newNode):
        if self.left is None:
            self.left = BinaryTree(newNode)
        else:
            tmp=self.left
            self.left = BinaryTree(newNode)
            self.left.left = tmp

    def insertRight(self,newNode):
        if self.right is None:
            self.right = BinaryTree(newNode)
        else:
            tmp=self.right
            self.right = BinaryTree(newNode)
            self.right.right = tmp