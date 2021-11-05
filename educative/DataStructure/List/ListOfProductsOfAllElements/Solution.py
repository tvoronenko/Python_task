#complexity time O(n)
#space complexity O(1)

class Solution:
    def find_product(self, lst):
        left = 1
        product= []
        for num in lst:
            product.append(left)
            left = left * num

        right = 1
        for i in range(len(lst)-1, -1, -1):
            product[i] *= right
            right *= lst[i]
        return product


if __name__ == '__main__':
    # begin
    s = Solution()
    assert s.find_product([1,2,3,4]) == [24,12,8,6]
    assert s.find_product([0, 1, 10, 100]) == [1000, 0, 0, 0]
    assert s.find_product([0, 2, 9, 0, 12, 25]) == [0, 0, 0, 0, 0, 0]