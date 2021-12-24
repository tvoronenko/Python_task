def binary_search(arr,item):
    left = 0
    right = len(arr) - 1
    while left <= right :
        mid = left + (right - left) // 2
        if arr[mid] == item:
            return True
        elif item < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return False


arr = [1,2,3,4,5,6,7,8,9]
assert binary_search(arr,1) == True
assert binary_search(arr,5) == True
assert binary_search(arr,8) == True
assert binary_search(arr,10) == False

