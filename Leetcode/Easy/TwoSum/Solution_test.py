from .Solution import Solution

def test_basic():
    solution = Solution()
    nums = [3, 2, 4]
    target = 6
    expected = [1,2]
    result = solution.twoSum(nums,target)
    assert expected == result