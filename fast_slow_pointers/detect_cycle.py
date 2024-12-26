'''
Check whether or not a linked list contains a cycle. If a cycle exists, return TRUE. Otherwise, return FALSE.
The cycle means that at least one node can be reached again by traversing the next pointer.

Traversal with a cycle:
Initially, both pointers traverse the list until they enter the cycle, taking at most O(n) steps.
Once inside the cycle, the pointers "chase" each other.
In the worst case, the fast pointer will catch up to the slow pointer after one complete cycle, which involves at most O(k) steps, where k is the size of the cycle.
Overall, this is still O(n) because k < n.
Total Time Complexity: O(n)

Total Space Complexity: O(1) (constant space).
'''
from DS.linked_list import LinkedList
class Solution:
    def detect_cycle(self, head):
        if head is None or head.next is None:
            return False
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False
       
if __name__ == '__main__':
    # begin
    s = Solution()
    a = LinkedList()
    b = LinkedList()
    a.create_linked_list([2,4,6,8,10])
    a.create_cycle(2)
    b.create_linked_list([1,3,5,7,9])
    assert (s.detect_cycle(a.head) == True)
    assert (s.detect_cycle(b.head) == False)

'''
Questions:
1. What does it mean for a linked list to have a cycle?
How would you define a cycle in terms of node traversal?
What conditions must be met for a cycle to exist?
2. What should the function return if a cycle is detected?
What should it return if no cycle is found?
Are there specific requirements for the return type (e.g., True/False, node reference, etc.)?
3. What are some edge cases to consider?
What if the linked list is empty?
What if there is only one node in the list?
What if the cycle involves all nodes, or only part of the list?
4. What algorithms or techniques can you use to detect a cycle?
What are the trade-offs between these methods (e.g., Floyd’s algorithm vs. hash table)?
5. Can you describe the high-level idea of your approach?
How would you explain the concept of "slow and fast pointers" or other methods to someone unfamiliar with them?
6. What’s the time and space complexity of your approach?
Why is Floyd’s algorithm 𝑂(1) in space, and why is it efficient?
7. How is the linked list represented in the problem?
Is it a custom Node class or a predefined structure?
Does the function take the head of the list as input?
8. Do you need to modify the linked list?
Should the solution preserve the original structure of the list?
9. How will you identify that two pointers have met in a cycle?
What does it mean for the "slow" and "fast" pointers to meet?
10 What happens if the list is very large?
Can your solution handle extremely large linked lists without running out of memory or taking too much time?
11. What if you needed to find the starting node of the cycle?
Could you extend your solution to determine where the cycle begins?
12. Can this algorithm be generalized to other structures, such as a directed graph?
How would cycle detection differ in other data structures?
13. What do you find challenging about detecting cycles in a linked list?
Are there any parts of this problem that might require extra attention or clarification?
14. How do you ensure that your solution is correct?
How will you test your implementation for correctness and handle edge cases?
15. Why do you think this problem is important in software development?
What real-world scenarios might involve detecting cycles?

Tests:
1. Basic Tests
No cycle (simple list):
Example: Linked list with nodes: 1 → 2 → 3 → 4 → 5 → None
Expected Output: False
Cycle exists:
Example: Linked list with nodes: 1 → 2 → 3 → 4 → 5 → (points back to 3)
Expected Output: True

2. Edge Cases
Empty list:
Example: None (head is None)
Expected Output: False
Single node with no cycle:
Example: 1 → None
Expected Output: False
Single node with a cycle:
Example: 1 → (points back to itself)
Expected Output: True
Two nodes without a cycle:
Example: 1 → 2 → None
Expected Output: False
Two nodes with a cycle:
Example: 1 → 2 → (points back to 1)
Expected Output: True

3. Complex Cycles
Cycle at the end:
Example: 1 → 2 → 3 → 4 → 5 → (points back to 2)
Expected Output: True
Cycle in the middle:
Example: 1 → 2 → 3 → 4 → 5 → (points back to 3)
Expected Output: True
Entire list is a cycle:
Example: 1 → 2 → 3 → (points back to 1)
Expected Output: True

4. Large Inputs
Large linked list with no cycle:
Example: A linked list with 1,000,000 nodes ending in None
Expected Output: False
Large linked list with a cycle:
Example: A linked list with 1,000,000 nodes, where the last node points back to the 500,000th node.
Expected Output: True

5. Invalid Inputs
Non-standard input:
Example: Input is None (or malformed input).
Expected Output: Should handle gracefully (return False or raise an appropriate exception).

Final Checklist of Edge Cases
Case                	          Description	                        Expected    Output
Empty list	                    No nodes	                            False
Single node, no cycle	        Single node with no next	            False
Single node, self-referential	Single node pointing to itself	        True
Two nodes, no cycle	            1 → 2 → None	                        False
Two nodes, cycle	            1 → 2 → (points back to 1)  	        True
Linear list	                    1 → 2 → 3 → 4 → None	                False
Cycle at the end            	1 → 2 → 3 → 4 → (points back to 2)	    True
Cycle in the middle	            1 → 2 → 3 → 4 → 5 → (points back to 3)	True
Entire list is a cycle      	1 → 2 → 3 → (points back to 1)      	True
Large list, no cycle	        1,000,000 nodes ending in None	        False
Large list, cycle	            1,000,000 nodes, cycle at the 500,000th node	True
Multi-node cycle	            Cycle involves part of the list     	True
Disconnected components     	Unconnected list segments	            Clarify with interviewer
Circular linked list	        Tail node points back to the head       Clarify with interviewer


'''