from Udemy_course.PythonforDSandA.LinkedList.LInkedList import Node


class OrderedList():
    def __init__(self):
        self.head = None

    def add(self,item):
        newNode = Node(item)
        cur = self.head
        prev = None
        while cur:
            if cur.value < item:
                prev = cur
                cur = cur.next
            else:
                break
        if prev == None:
            newNode.next = self.head
            self.head = newNode
        else:
            newNode.next = cur
            prev.next = newNode

    def search(self,item):
        cur = self.head
        while cur:
            if cur.value == item:
                return True
            if cur.value > item:
                return False
            cur = cur.next
        return False

    def size(self):
        cur = self.head
        count = 0
        while cur:
            count +=1
            cur = cur.next
        return count

    def remove(self,item):
        cur = self.head
        prev = None
        while cur:
            if cur.value == item:
                break
            prev = cur
            cur = cur.next

        if cur is None:
            raise ValueError("No such item")
        if prev is None:
            self.head = cur.next
        else:
            prev.next = cur.next





my_list = OrderedList()
my_list.add(31)
my_list.add(77)
my_list.add(17)
my_list.add(93)
my_list.add(26)
my_list.add(54)
print(my_list.search(17))
print(my_list.size())
my_list.remove(17)
print(my_list.search(17))
print(my_list.size())