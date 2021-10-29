
class Solution:
    def merge_lists(self,lst1, lst2):
        output = []
        i,j = 0, 0
        while i < len(lst1) and j < len(lst2):
            if lst1[i] <= lst2[j]:
                output.append(lst1[i])
                i += 1
            else:
                output.append(lst2[j])
                j += 1

        while i < len(lst1):
            output.append(lst1[i])
            i += 1
        while j < len(lst2):
            output.append(lst2[j])
            j += 1

        return output

    def merge_lists_in_place(self,lst1, lst2):
        i, j = 0, 0
        while i < len(lst1) and j < len(lst2):
            if lst1[i] <= lst2[j]:
                i += 1
            else:
                lst1.insert(i,lst2[j])
                j += 1
                i += 1

        while j < len(lst2):
            lst1.append(lst2[j])
            j += 1
        return lst1

if __name__ == '__main__':
    # begin
    s = Solution()
    list1 = [1, 3, 4, 5]
    list2 = [2, 6, 7, 8]
    arr = [1, 2, 3, 4, 5, 6, 7, 8]
    assert s.merge_lists(list1,list2) == arr
    assert s.merge_lists_in_place(list1, list2) == arr