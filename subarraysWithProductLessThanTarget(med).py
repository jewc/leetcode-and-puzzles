# find Subarrays with product less than target

# Problem Statement
# Given an array with positive numbers and a positive target number,
# find all of its contiguous subarrays whose product is less than the target number.

# Time Complexity
# the main for-loop managing the sliding window takes O(N) but creating subarrays can take up
# to O(N^2) in the worst case. Therefore, our algorithm will take O(N^3)


from collections import deque

def find_subarrays(arr, target):
    result = []
    product = 1
    left = 0

    for right in range(len(arr)):
        product *= arr[right]

        # since the product of all numbers from left to right is less than the target,
        # all subarrays from left to right will have a product less than the target too
        # To avoid duplicates, we will start with a subarray containing only arr[right]
        # and then extendt it

        while (product >= target and left <= right):
            product /= arr[left]
            left += 1
        temp_list = deque()

        for i in range(right, left-1, -1):
            temp_list.appendleft(arr[i])
            result.append(list(temp_list))

    return result

def main():
  print(find_subarrays([2, 5, 3, 10], 30))
  print(find_subarrays([8, 2, 6, 5], 50))


main()
