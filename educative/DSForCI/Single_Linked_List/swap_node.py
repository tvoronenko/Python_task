from DS.linked_list import Node
from DS.linked_list import  LinkedList
class Solution:
    def swap_nodes(self,ll, key1, key2):
        if ll.head == None:
            return
        if key1 == key2:
            return
        cur1 = ll.head
        prev1 = None
        while cur1 and cur1.data == key1:
            prev1 = cur1
            cur1 = cur1.next
        if not cur1 :
            print("No item with " + key1)

        cur2 = ll.head
        prev2 = None
        while cur2 and cur2.data == key2:
            prev2 = cur2
            cur2 = cur2.next
        if not cur2 :
            print("No item with " + key2)


        if prev1:
            prev1.next = cur2
        else:
            ll.head = cur2
        if prev2:
            prev2.next = cur1
        else:
            ll.head = cur1

        cur1.next, cur2.next = cur2.next, cur1.next






if __name__ == '__main__':
    # begin
    s = Solution()
    llist = LinkedList()
    llist.append("A")
    llist.append("B")
    llist.append("C")
    llist.append("D")

    print("Original List")
    llist.print_list()
    s.swap_nodes(llist, "B", "C")

    llist.print_list()
    #assert (s.swap_nodes(llist,"B", "C") == "A->C->B->D->NULL")


