class Queue():

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self,item):
        self.items.insert(0,item)

    def addRear(self,item):
        self.items.append(item)

    def removeRear(self):
        return self.items.pop()

    def removeFront(self):
        return self.items.pop(0)

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)