#complexity time O(n)
#space complexity O(n)

class Solution:
    def find_sum(self,lst,k):
        hash_table = set()
        for i, num in enumerate(lst):
            target = k - num
            if target in hash_table:
                return [target, num]
            else:
                hash_table.add(num)
        return []


if __name__ == '__main__':
    # begin
    s = Solution()
    assert s.find_sum([1,21,3,14,5,60,7,6],81) == [21,60]