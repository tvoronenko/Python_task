class Solution:
    def remove_even(self,lst):
        return [i for i in lst if i % 2 != 0]




if __name__ == '__main__':
    # begin
    s = Solution()
    arr_input = [-189, -80, -97, -160, 29, 179, 87, 27, -166, -199, 107, 155, -58, 57, -186, 7, 86, 103, 159, -21, 180, 32, -163, 177, -44, 126, 15, 132, -71, 146, 112, -36, -6, 127, 96, -10, 50, 47]
    arr_output = [-189, -97, 29, 179, 87, 27, -199, 107, 155, 57, 7, 103, 159, -21, -163, 177, 15, -71, 127, 47]
    print(s.remove_even(arr_input))
    assert s.remove_even(arr_input) == arr_output
