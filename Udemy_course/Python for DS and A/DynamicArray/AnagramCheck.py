


"""
RUN THIS CELL TO TEST YOUR SOLUTION
"""
from collections import Counter


def anagram(s1, s2):
     # Remove spaces and lowercase letters
    s1 = s1.replace(' ','').lower()
    s2 = s2.replace(' ','').lower()

    if len(s1) != len(s2):
        return False

    count = Counter(s1)
    for ch in s2:
        if ch in count:
            count[ch] -= 1
        else:
            return False
        if count[ch] == 0:
            del count[ch]
    if len(count) != 0:
        return False
    return True




class AnagramTest(object):

    def test(self, sol):
        assert sol('go go go', 'gggooo')==True
        assert sol('abc', 'cba')== True
        assert sol('hi man', 'hi     man')== True
        assert sol('aabbcc', 'aabbc')==False
        assert sol('123', '1 2')== False
        print(        "ALL TEST CASES PASSED")


# Run Tests
t = AnagramTest()
t.test(anagram)