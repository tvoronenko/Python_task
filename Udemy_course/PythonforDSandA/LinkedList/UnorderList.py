from Udemy_course.PythonforDSandA.LinkedList.LInkedList import Node

class UnorderList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self,item):
        tmp = Node(item)
        tmp.next = self.head
        self.head = tmp

    def size(self):
        cur = self.head
        count = 0
        while cur:
            count +=1
            cur = cur.next
        return count

    def search(self,item):
        cur = self.head
        while cur:
            if cur.value == item:
                return True
            cur = cur.next
        return False

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






my_list = UnorderList()
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
