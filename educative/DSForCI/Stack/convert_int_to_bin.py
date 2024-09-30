#Time:
#Space:
'''
Problem: use the stack data structure to convert integer values to their binary equivalent.


'''

from DS.stack import Stack
class Solution:
    def convert_int_to_bin(self,dec_num):
        result_list = []
        while dec_num != 0 :
            reminder = dec_num % 2
            dec_num = dec_num // 2
            if reminder % 2 == 0:
                result_list.append("0")
            else:
                result_list.append("1")
        return "".join(result_list[::-1])

    def convert_int_to_bin_stack(self,dec_num):
        s = Stack()
        while dec_num != 0 :
            reminder = dec_num % 2
            dec_num = dec_num // 2
            if reminder % 2 == 0:
                s.push("0")
            else:
                s.push("1")
        bit_num = ""
        while not s.is_empty():
            bit_num += s.pop()
        return bit_num




if __name__ == '__main__':
    # begin
    s = Solution()
    assert (s.convert_int_to_bin(63) == "111111")
    assert (s.convert_int_to_bin(72) == "1001000")
    assert (s.convert_int_to_bin(92) == "1011100")
    assert (s.convert_int_to_bin(25) == "11001")

    assert (s.convert_int_to_bin_stack(63) == "111111")
    assert (s.convert_int_to_bin_stack(72) == "1001000")
    assert (s.convert_int_to_bin_stack(92) == "1011100")
    assert (s.convert_int_to_bin_stack(25) == "11001")
