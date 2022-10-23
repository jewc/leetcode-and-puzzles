# Triplet Sum to Zero

# Problem Statement
# Given an array of unsorted numbers, find all unique triplets in it that
# add up to zero.

# Time complexity#
# Sorting the array will take O(N * logN).
# The searchPair() function will take O(N).
#
# As we are calling searchPair() for every number in the input array, this means
# that overall searchTriplets() will take O(N * logN + N^2)
# which is asymptotically equivalent to O(N^2).
#
# Space complexity#
# Ignoring the space required for the output array, the space complexity of the above algorithm will be O(N)
# which is required for sorting.

# first sort the array. iterate through it taking one number at a times
# assume we are 'x' in first iteration. we then need to find 'y' and 'z' such that
# x + y + z = 0
#
# we also need to find all unique triplets. To achieve this, skip any duplicate number

def search_triplets(arr):
    arr.sort()
    triplets = [] # stores the valid triplets

    for i in range(len(arr)):
        # skip same elements to avoid duplicate triplets
        if i > 0 and arr[i] == arr[i-1]:
            continue
        # find a pair whose sum is equal to -x , such that y + z = -x
        # and x + y + z = 0
        search_pair(arr, -arr[i], i+1, triplets)
    return triplets

def search_pair(arr, target_sum, left, triplets):
    right = len(arr) - 1
    while (left < right):

        current_sum = arr[left] + arr[right]

        if current_sum == target_sum: # if found the triplet
            triplets.append([-target_sum, arr[left], arr[right]])
            left += 1
            right -= 1

            # skip the element to avoid duplicate triplets
            while left < right and arr[left] == arr[left - 1]:
                left += 1

            # skip the same element to avoid duplicate triplets
            while left < right and arr[right] == arr[right + 1]:
                right -= 1

        # we need a pair with a larger sum
        elif target_sum > current_sum:
            left += 1
        # we need a pair with a smaller sum
        else:
            right -= 1

def main():
  print(search_triplets([-3, 0, 1, 2, -1, 1, -2]))
  print(search_triplets([-5, 2, -1, -2, 3]))

main()
