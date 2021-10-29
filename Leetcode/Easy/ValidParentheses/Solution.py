class Solution:
    def isValid(self, s: str) -> bool:
        if s == "":
            return True
        # lengh of valid string should be divided by 2
        if len(s) % 2 == 1:
            return False
        # create hash table of open and close parentheses
        table = {"]":"[","}":"{",")":"("}
        # stack for stroring open  parentheses
        stack = []
        for ch in s:
            # strore parentheses if it is open
            if ch in table.values():
                stack.append(ch)
            else:
                # if parentheses is closed type and stack if empty so str in invalid
                if stack:
                    #check that we can find correct open parentheses for this type of close parentheses
                    if stack.pop() != table[ch]:
                        return False
                else:
                    return False
        # if we go thru all char and stack is  not empty str is invalid
        if len(stack) != 0:
            return False
        return True



if __name__ == '__main__':
    # begin
    s = Solution()
    assert s.isValid("()") == True
    assert s.isValid("()[]{}") == True
    assert s.isValid("(]") == False
    assert s.isValid("([)]") == False
    assert s.isValid("{[]}") == True
    assert s.isValid("))") == False
    assert s.isValid("((") == False
