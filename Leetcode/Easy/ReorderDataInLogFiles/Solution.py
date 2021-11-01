#complexity time O()
#space complexity O()
from collections import OrderedDict
class Solution:
    def reorderLogFiles(self, logs):
        dict_log_digit = []
        dict_log_letter = []
        for log in logs:
            list_word = log.split(" ",1)
            key = list_word[0]
            if list_word[1][0].isdigit():
                dict_log_digit.append(log)
            else:
                # first is content then key, for sorting
                dict_log_letter.append((list_word[1],key))
        dict_log_letter.sort()
        return [" ".join([log[1],log[0]]) for log in dict_log_letter] + dict_log_digit

    # using sorting key
    def reorderLogFiles_another(self, logs):
        def get_key_rule(log):
          # we need only one split between key and rest of log
            _id, remain = log.split(" ",maxsplit=1)
            if remain[0].isdigit():
                return (1,)
            else:
                return (0,remain,_id)


        return sorted(logs, key = get_key_rule)

if __name__ == '__main__':
    # begin
    s = Solution()
    assert s.reorderLogFiles(["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]) == ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
    assert s.reorderLogFiles(["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]) == ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]
    assert s.reorderLogFiles(["1 n u", "r 527", "j 893", "6 14", "6 82"]) == ["1 n u","r 527","j 893","6 14","6 82"]
