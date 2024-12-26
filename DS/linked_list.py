""" Linked List Data Structure.
"""
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

    def create_list(self):
        list_curr = []
        cur = self
        while cur:
            if cur.next:
                list_curr.append(cur.data)
            else:
                list_curr.append(cur.data)
            cur = cur.next
        return list_curr


class LinkedList:
    def __init__(self):
        self.head = None

    #The append method will insert an element at the end of the linked list.
    def append(self, data):
        #if no head -> add head
        if not self.head:
            self.head = Node(data)
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = Node(data)

    # insert_node_at_head method will insert a LinkedListNode at head
    # of a linked list.
    def insert_node_at_head(self, node):
        if self.head:
            node.next = self.head
            self.head = node
        else:
            self.head = node
        # create_linked_list method will create the linked list using the
        # given integer array with the help of InsertAthead method.

    def create_linked_list(self, lst):
        self.head = None
        for x in reversed(lst):
            new_node = Node(x)
            self.insert_node_at_head(new_node)

    def create_list(self):
        list_curr = []
        cur = self.head
        while cur:
            if cur.next:
                list_curr.append(cur.data)
            else:
                list_curr.append(cur.data)
            cur = cur.next
        return list_curr


    #The prepend method will insert an element at the beginning of the linked list
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self, prev_node, data):
        if not prev_node:
            print("Prev node doesn't exist")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def print_list(self):
        cur = self.head
        while cur:
            if cur.next:
                print(cur.data, end = "->")
            else:
                print(cur.data, end = "->NULL\n")
            cur = cur.next

    # __str__(self) method will display the elements of linked list.
    def __str__(self):
        result = ""
        temp = self.head
        while temp:
            result += str(temp.data)
            temp = temp.next
            if temp:
                result += "->"
        result += "->NULL"
        return result

    def delete_node(self, key):
        if self.head and self.head.data == key:
            self.head = self.head.next
        else:
            cur = self.head
            prev = None
            while cur:
                if cur.data == key:
                    prev.next = cur.next
                    return
                prev = cur
                cur = cur.next

    def delete_node_at_pos(self, pos):
        if not self.head:
            return
        if pos == 0:
            self.head = self.head.next
        else:
            cur = self.head
            i = 0
            prev = None
            while cur:
                if i == pos:
                    prev.next = cur.next
                    return
                prev = cur
                cur = cur.next
                i += 1
            if i <= pos:
                print("No such index")

    def len_iterative(self):
        size = 0
        cur = self.head
        while cur:
            size += 1
            cur = cur.next
        return size

    def len_recursive(self, node):
        if not node:
            return 0
        return self.len_recursive(node.next)+1

    def swap_nodes(self, key1, key2):
        if not self.head:
            return
        # Check if key_1 and key_2 are the same element. If they are, we return from the method
        if key2 == key1:
            return

        cur1 = self.head
        cur2 = self.head
        prev1 = None
        prev2 = None
        # We loop through the linked list using the while loop which runs while cur1 is not at the end of the linked list
        # or it is not equal to the key1 that we seek. In the while loop, we keep updating the prev1 node equal
        # to the cur1 and the cur1 to the next node in the linked list.
        while cur1 and cur1.data != key1:
            prev1 = cur1
            cur1 = cur1.next
        # element with key1 not found
        if not cur1:
            print("No key1")
            return
        # We loop through the linked list using the while loop which runs while cur2 is not at the end
        # of the linked list, or it is not equal to the key2 that we seek. In the while loop, we keep
        # updating the prev2 node equal to the cur2 and the cur2 to the next node in the linked list.
        while cur2 and cur2.data != key2:
            prev2 = cur2
            cur2 = cur2.next
        # element with key2 not found
        if not cur2:
            print("No key2")
            return
        # we will check if the previous nodes of the current nodes exist or not. If they don’t exist and are None,
        # then the node without the previous node is the head node.
        # if prev1 does not exist, it implies that cur1 is the head node and
        # we set self.head to its new value, i.e., cur2
        if not prev1:
            self.head = cur2
        else:
            # initially prev1.next was pointed to cur1
            prev1.next = cur2
        # the same for cur2 as above for cur1
        if not prev2:
            self.head = cur1
        else:
            prev2.next = cur1
        # Now that we have handled the previous nodes that will point to the different nodes,
        # we’ll swap the next of cur1 with the next of the cur2 and vice versa.
        # We code this swap using the Python shorthand.
        cur2.next,cur1.next = cur1.next, cur2.next

    def reverse_iterative(self):
        cur = self.head
        prev = None
        next = self.head
        while next and next.next:
            cur.next = prev
            prev = cur
            next = next.next
            cur = next
        return next


    def reverse_recursive(self):
        pass

    def create_cycle(self, position):
        """
        Creates a cycle in the linked list by connecting the tail node
        to the node at the given position (0-indexed).
        """
        if position < 0:
            return
        cycle_start = None
        current = self.head
        index = 0
        while current.next:
            if index == position:
                cycle_start = current
            current = current.next
            index += 1
        current.next = cycle_start  # Connect tail to the node at 'position'

llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")

#llist.reverse_recursive()

#llist.print_list()

#llist.reverse_iterative()

#llist.print_list()