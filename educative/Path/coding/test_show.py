def func(nums):
    current_index = 0
    index_zero = 0
    while current_index < len(nums):
        if nums[current_index] != 0:
            nums[index_zero], nums[current_index] = nums[current_index], nums[index_zero]
            index_zero =+ 1
        current_index += 1
    print(nums)

func([0,1,0,2,3])

