# Given an array of positive numbers and a positive number ‘k,’
# find the maximum sum of any contiguous subarray of size ‘k’.
# Easy

# brute force
def max_sub_array_of_size_k_bf(k, arr):
    max_sum = 0
    window_sum = 0

    # increment window_start
    # find sum of elements of subarray size k
    for i in range(len(arr) - k + 1):
        window_sum = 0

        # sum across the window
        for j in range(i, i+k):
            window_sum += arr[j]
        max_sum = max(max_sum, window_sum)
    return max_sum

# sliding window
def max_sub_array_of_size_k_sw(k, arr):
    max_sum = 0
    window_sum = 0
    window_start = 0

    for window_end in range(len(arr)):
        window_sum += arr[window_end] # add the next element

        # slide the window, we don't need to slide if we've
        # not hit the required window size of 'k'

        if window_end >= k-1:
            max_sum = max(max_sum, window_sum)
            window_sum -= arr[window_start] # subtract the outgoing element
            window_start += 1 # slide the window ahead
    return max_sum

def main():
  print("Maximum sum of a subarray of size K: " + str(max_sub_array_of_size_k_bf(3, [2, 1, 5, 1, 3, 2])))
  print("Maximum sum of a subarray of size K: " + str(max_sub_array_of_size_k_sw(2, [2, 3, 4, 1, 5])))

main()
