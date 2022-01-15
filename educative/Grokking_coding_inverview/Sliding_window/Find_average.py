'''Given an array, find the average of all contiguous subarrays of size ‘K’ in it.'''

def find_averages_of_subarrays(K, arr):
    window_start = 0
    window_sum = 0.0
    window_end = 0
    result = []
    while window_end < len(arr):
        window_sum += arr[window_end]
        window_end += 1
        if window_end >= K:
            aver = window_sum / K
            result.append(aver)
            window_sum -= arr[window_start]
            window_start += 1


    return result


def main():
  result = find_averages_of_subarrays(5, [1, 3, 2, 6, -1, 4, 1, 8, 2]) #Averages of subarrays of size K: [2.2, 2.8, 2.4, 3.6, 2.8]
  print("Averages of subarrays of size K: " + str(result))


main()