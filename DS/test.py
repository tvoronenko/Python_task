class Solution:
    def findWord(self,  inputString, searchWord):
        list_usage = []
        ind = 0
        indSearch = 0
        for i in range(len(inputString)):
            if indSearch < len(searchWord) and inputString[i] == searchWord[indSearch] :
                indSearch += 1
            else:
                if indSearch == len(searchWord) and inputString[i] in " ,.!?":
                    list_usage.append(i - len(searchWord))
                indSearch = 0
        if indSearch == len(searchWord):
            list_usage.append(len(inputString) - len(searchWord))
        return list_usage

if __name__ == '__main__':
    # begin
    s = Solution()
    assert (s.findWord( "test_show.py testing word test_show.py of word test_show.py", "test_show.py") == [0, 18, 31])