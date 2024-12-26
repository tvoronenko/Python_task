''' Write an algorithm to determine if a number n is a happy number.
We use the following process to check if a given number is a happy number:

Starting with the given number n, replace the number with the sum of the squares of its digits.
Repeat the process until:
The number equals 1, which will depict that the given number n is a happy number.
The number enters a cycle, which will depict that the given number n is not a happy number.
Return TRUE if n is a happy number, and FALSE if not.

Time Complexity: 
O(log(n))
Space Complexity: 
O(1)
'''
class Solution:
    def is_happy_number(self, num):
        # Handle edge cases explicitly
        if num == 1:  # Base case
            return True
        if num == 0:  # Handle zero
            return False
    
        if not isinstance(num, int) or num < 1:  # Validate input
            return False  # Invalid input is not a happy number
        
        # Use the fast and slow pointer approach
        slow_pointer = num # Move slow pointer one step
        fast_pointer = self.sum_sq_digit(num) # Move fast pointer two steps
        if fast_pointer == 1:  #If fast pointer reaches 1, it's a happy number
            return True
        while fast_pointer != 1 and fast_pointer != slow_pointer: # If slow and fast pointers meet, there's a cycle
            slow_pointer = self.sum_sq_digit(slow_pointer)
            fast_pointer = self.sum_sq_digit(self.sum_sq_digit(fast_pointer))
            if fast_pointer == 1:  #If fast pointer reaches 1, it's a happy number
                return True
        return False # If there's a cycle, it's not a happy number

    def is_happy_number_set(self, num):
        seen = set()  # To track numbers we've already seen

        # Continue the process until n equals 1 or we detect a cycle
        while n != 1 and n not in seen:
            seen.add(n)  # Add the number to the set
            n = self.sum_sq_digit(n)  # Update n to the sum of squares of its digits

        return n == 1  # If n == 1, it's a happy number; otherwise, it's not
    
    def sum_sq_digit(self, num):
        sum_sq = 0
        while num > 0:
            digit = num % 10
            sum_sq += digit * digit
            num //= 10
        return sum_sq

if __name__ == '__main__':
    # begin
    s = Solution()
    assert (s.is_happy_number(23) == True)
    assert (s.is_happy_number(16) == False)
    assert (s.is_happy_number(28 ) == True)
    assert (s.is_happy_number(4) == False)
    assert(s.is_happy_number(2147483646) == False)
    assert(s.is_happy_number(1) == True)
    assert(s.is_happy_number_set(1) == True)
    assert(s.is_happy_number_set(2147483646) == False)    
'''
Questions:
1. Input Constraints:
What is the range of the input number n? Can n be negative or zero, or is it guaranteed to be a positive integer?
For example: Is n = 0 valid? What should be the output for n = 0?

2. Output Expectations:
Should we return True/False, or are there any specific values we need to output (e.g., "Yes"/"No")?

3. Edge Cases:
Are there any specific edge cases to handle, such as small numbers like 1 or large numbers with many digits?

4. Behavior on Invalid Input:
If the input is invalid (e.g., non-integer, negative), how should we handle it? Should we validate the input or assume it is always valid?

5. Cycle Detection Approach:
Should we use the fast-and-slow pointer approach or a set to track visited numbers?
Do you have a preference for one over the other based on performance or clarity?

6. Efficiency Expectations:
Are there specific constraints on time or space complexity that we should optimize for

7. Helper Functions:
Is it acceptable to use a helper function (e.g., to calculate the sum of squares of digits)?
Should the helper function be explicitly defined, or can it be part of the main logic?

8. Code Structure:
Should we wrap the logic in a specific class or keep it as a standalone function?

9. Follow-Up Questions:
Should we expect to discuss extensions to the problem, such as determining the cycle length if the number is not happy?
Would you like me to explain how I handle large inputs and ensure the solution terminates?

Tests:
Happy Number:
assert is_happy_number(19) == True  # 19 is a happy number
assert is_happy_number(1) == True   # 1 is a happy number

Unhappy Number:
assert is_happy_number(2) == False  # 2 is not a happy number
assert is_happy_number(20) == False # 20 is not a happy number

Small Numbers:
assert is_happy_number(0) == False  # 0 is not a happy number (if allowed as input)
assert is_happy_number(7) == True   # Single-digit happy number
assert is_happy_number(4) == False  # Single-digit unhappy number

Large Happy Numbers:
assert is_happy_number(100) == True  # 100 is a happy number
assert is_happy_number(986543210) == True  # Random large happy number

Cycle Test (Unhappy Numbers):
Check a number known to fall into a cycle:
assert is_happy_number(116) == False  # Falls into a cycle
assert is_happy_number(145) == False  # Falls into a cycle

Repeated Calculations:
Verify that repeated inputs yield consistent results:
assert is_happy_number(19) == True
assert is_happy_number(19) == True  # Test repeated calls with the same input

Very Large Number:
Test the function with a very large number to ensure it handles high values:
assert is_happy_number(987654321) == False  # Stress test with a large input

Negative Numbers:
If negative numbers are allowed (or explicitly disallowed), define behavior:
assert is_happy_number(-19) == False  # Negative numbers are not happy numbers

'''