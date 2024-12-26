'''
Given a singly linked list, remove the nth node from the end of the list and return its head.

The time complexity is O(n), where n is the number of nodes in the linked list.
The space complexity is O(1) because we use constant space to store two pointers.
'''
from DS.linked_list import LinkedList
class Solution:
    def remove_nth_last_node(self, head, n):
        left, right = head, head
        # Move right pointer n elements away from the left pointer.
        for i in range(n):
            right = right.next
        # Removal of the head node.
        if not right:
            return head.next
        # Move both pointers until right pointer reaches the last node.
        while right.next:
            right = right.next
            left = left.next

            # At this point, left pointer points to (n-1)th element.
            # So link it to next to next element of left.
        left.next = left.next.next
        return head

if __name__ == '__main__':
    # begin
    s = Solution()
    a = LinkedList()
    b = LinkedList()
    a.create_linked_list([23, 28, 10, 5, 67, 39, 70, 28])
    b.create_linked_list([23, 28, 10, 5, 67, 39, 28])
    assert (s.remove_nth_last_node(a.head , 2).create_list() == b.head.create_list())
    a.create_linked_list([34,53,6,95,38,28,17,63,16,76])
    b.create_linked_list([34,53,6,95,38,28,17,16,76])
    assert (s.remove_nth_last_node(a.head , 3).create_list() == b.head.create_list())
    a.create_linked_list([288,224,275,390,4,383,330,60,193])
    b.create_linked_list([288,224,275,390,4,330,60,193])
    assert (s.remove_nth_last_node(a.head , 4).create_list() == b.head.create_list())
    a.create_linked_list([1,2,3,4,5,6,7,8,9])
    b.create_linked_list([1,2,3,4,5,6,7,8])
    assert (s.remove_nth_last_node(a.head , 1).create_list() == b.head.create_list())
    a.create_linked_list([69,8,49,106,116,112] )
    b.create_linked_list([8,49,106,116,112])
    assert (s.remove_nth_last_node(a.head , 6).create_list() == b.head.create_list())
'''
Questions:
1. Clarifying Input and Output
What should I return if the list has fewer than n nodes? Should I return the original list, or is it guaranteed that n is always valid?
What should I return if n equals the length of the list? Should I remove the head in this case, or is there a special case to handle?
Can n be zero? Is this a valid input, and how should I handle it if so?
2. Edge Cases
What should I do if the list contains only one node? If n = 1, should I return an empty list (i.e., None), or is there any other specific behavior required?
What if n is greater than the length of the list? Should I assume n will always be a valid index from the end, or should I handle cases where n exceeds the list length?
3. Performance Requirements
Are there any constraints on time and space complexity? Should I aim for a solution that runs in a single pass (O(n) time complexity) or is a two-pass solution acceptable? Is there any limitation on the amount of extra space I can use?
4. List Modifications
Is it acceptable to modify the input list in place? Should I aim to remove the node in-place, or is creating a new list and returning it an option?
Do I need to handle memory cleanup for the removed node? In languages like C/C++, manual memory management is required, but this is less of a concern in garbage-collected languages like Python.
5. Clarification on Linked List Definition
Can the list contain null/None nodes? Should I handle null nodes within the list, or can I assume the list will be properly constructed with non-null nodes?
Is the list circular or guaranteed to be a standard singly linked list? Just to confirm the structure of the list being used.

Tests:
1. General Case
2. Single Node
3. Remove Head
4. List of Size n
5. Remove Last Node
6. Large List
7. Edge Case: Remove From Start in Large List
8. Edge Case: Remove Last in Large List
1. Empty List 
2. Invalid n 
'''