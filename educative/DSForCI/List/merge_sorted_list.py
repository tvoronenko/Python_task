#Time: O(m(n+m)) =>  O(n^2)
#Space: O(m)
class Solution:
    def merge_lists(self,lst1, lst2):
        i, j = 0, 0
        if len(lst1) == 0:
            return lst2
        if len(lst2) == 0:
            return lst1
        while i < len(lst1) and j < len(lst2):
            if lst1[i] <= lst2[j]:
                i += 1
            else:
                lst1.insert(i, lst2[j])
                i += 1
                j += 1
        if j < len(lst2):
            lst1.extend(lst2[j:])
        return lst1




if __name__ == '__main__':
    # begin
    s = Solution()
    assert (s.merge_lists([1,3,4,5],[2,6,7,8]) == [1, 2, 3, 4, 5, 6, 7, 8])
    assert (s.merge_lists([],[]) ==[])
    assert (s.merge_lists([],[1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5])
    assert (s.merge_lists([1, 4, 45, 63],[]) == [1, 4, 45, 63])
    assert (s.merge_lists([4, 4, 4, 4, 4, 4, 4],[4, 4, 4, 4, 4, 4, 4]) == [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4])
    assert (s.merge_lists([-133, -100, 0, 4],[-2000, 2000]) == [-2000, -133, -100, 0, 4, 2000])
