
"""
RUN THIS CELL TO TEST YOUR SOLUTION
"""
def rev_word(s):
    words = []
    i = 0
    while i < len(s):
        if not s[i].isspace():
            j = i + 1
            while j < len(s) and s[j] != ' ':
                j += 1
            words.append(s[i:j])
            i = j
        else:
            i += 1

    for i in range(len(words)//2):
        words[i],words[-(i+1)] = words[-(i+1)],words[i]
    return " ".join(words)


from nose.tools import assert_equal

class ReversalTest(object):

    def test(self ,sol):
        assert_equal(sol('    space before') ,'before space')
        assert_equal(sol('space after     ') ,'after space')
        assert_equal(sol('   Hello John    how are you   ') ,'you are how John Hello')
        assert_equal(sol('1') ,'1')
        print("ALL TEST CASES PASSED")

# Run and test_show.py
t = ReversalTest()
t.test(rev_word)