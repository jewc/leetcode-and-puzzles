# smallest subarray with a greatest sum
# easy

import math

def smallest_subarray_sum(s,arr):
    window_start = 0
    window_sum = 0
    min_length = math.inf

    for window_end in range(0, len(arr)):
        window_sum += arr[window_end] # add next element

    # shrink window as small as possible until window_sum
    # is smaller than s

        while window_sum >= s:
            # check and store min_length
            min_length = min(min_length, window_end - window_start + 1)
            # shift window sum by subtracting window_start from window_sum
            window_sum -= arr[window_start]
            # increment window_start by 1
            window_start += 1

    if min_length == math.inf:
        return 0
    else:
        return min_length

def main():
    print("Smallest subarray length: " + str(smallest_subarray_sum(7, [2, 1, 5, 2, 3, 2])))
    print("Smallest subarray length: " + str(smallest_subarray_sum(8, [3, 4, 1, 1, 6])))
    print("Smallest subarray length: " + str(smallest_subarray_sum(8, [2, 1, 5, 2, 3, 2])))

main()
