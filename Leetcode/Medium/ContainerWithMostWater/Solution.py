#complexity time O(n)
#space complexity O(1)

class Solution:
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        max_square = 0
        # there is two pointer, left and right side of container
        while left < right:
            # calc area using minimum lengh side
            current_square = min(height[left], height[right]) * (right - left)
            # select max from current area and prev.
            max_square = max(current_square,max_square)
            # compare two sides and move smaller one. No sense to move bigger side because area probably will be smaller than current
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_square


if __name__ == '__main__':
    # begin
    s = Solution()
    assert s.maxArea([1,8,6,2,5,4,8,3,7]) == 49
    assert s.maxArea([1,1]) == 1
    assert s.maxArea([4,3,2,1,4]) == 16
    assert s.maxArea([1,2,1]) == 2