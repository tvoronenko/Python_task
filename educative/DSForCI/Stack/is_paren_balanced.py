#Time:
#Space:
#Problem: determine whether or not a string has balanced usage of brackets by using a stack.
from DS.stack import Stack
class Solution:
    def is_paren_balanced(self,paren_string):
        s = Stack()
        dict_ = {')':'(', ']':'[', '}':'{'}
        for i in paren_string:
            if s.is_empty() and i in dict_.keys():
                return False
            if i in dict_.keys() and s.pop() != dict_[i]:
                return False
            if i not in dict_.keys():
                s.push(i)
        return s.is_empty()




if __name__ == '__main__':
    # begin
    s = Solution()
    assert (s.is_paren_balanced("(((({}))))") == True)
    assert (s.is_paren_balanced("[][]]]") == False)
    assert (s.is_paren_balanced("[][]") == True)
    assert (s.is_paren_balanced("{()()}") == True)
