# Given an array, find the average of each subarray of ‘K’ contiguous elements in it.
# brute force
def find_average_of_subarrays_bf(k, arr):
    # array for result
    result = []

    for i in range(len(arr)-k+1):
        # find sum of next 'K' elements
        _sum = 0.0
        for j in range(i, i+k):
            _sum += arr[j]
        result.append(_sum/k)

    return result

def find_average_of_subarrays_sw(k, arr):
    result = []
    windowSum = 0.0
    windowStart = 0

    for windowEnd in range(len(arr)):
        windowSum += arr[windowEnd] # add next element

        # slide the window, we don't need to slide if we've hit
        # the required window size of 'k'
        if windowEnd >= k - 1:
            result.append(windowSum/k) # calculate the average
            windowSum -= arr[windowStart] # calculate the element going out
            windowStart += 1 # slid the window ahead
    return result

def main():
    result = find_average_of_subarrays_bf(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
    print("Brute force: Averages of subarray of size K:" + str(result))

    result2 = find_average_of_subarrays_sw(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
    print("Sliding Window: Averages of subarray of size K:" + str(result2))

main()
