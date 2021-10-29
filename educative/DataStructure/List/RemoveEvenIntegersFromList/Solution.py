#complexity time O(n)
#complexity space O(1)
class Solution:
    def remove_even(self,lst):
        return [x for x in lst if x % 2 != 0]

    def remove_even_bits(self,lst):
        return [x for x in lst if (x & 1) == 1]

if __name__ == '__main__':
    # begin
    s = Solution()
    print(s.remove_even([3, 2, 4])) #[3]
    print(s.remove_even([2,7,11,15]))  # [7,11,15]
    assert s.remove_even([-12, -106, -118, 49, -77, 16, 137, 168, -112, 162, -75, -128, -42, 141, 76, 146, 80, -125, -91, -73, -32, -68,
         -19, -135, -124, -39, 19, 56, 169, -36, 59, 191, -117, 5, 109, -137]) == [49, -77, 137, -75, 141, -125, -91, -73, -19, -135, -39, 19, 169, 59, 191, -117, 5, 109, -137]
    assert s.remove_even([3, 2, 4]) == [3]
    assert s.remove_even([2,7,11,15]) == [7,11,15]

    print(s.remove_even_bits([3, 2, 4]))  # [3]
    print(s.remove_even_bits([2, 7, 11, 15]))  # [7,11,15]
    assert s.remove_even_bits([3, 2, 4]) == [3]
    assert s.remove_even_bits([2, 7, 11, 15]) == [7, 11, 15]