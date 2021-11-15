class Queue():

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self,item):
        self.items.indert(0,item)

    def dequeue(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

s = Queue()
print(s.isEmpty())
s.enqueue(1)
s.enqueue(2)
print(s.isEmpty())
print(s.size())
print(s.peek())
print(s.dequeue())
print(s.size)
print(s.peek())
