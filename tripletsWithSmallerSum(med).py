# Triplets with smaller sum
# medium

# Problem Statement
# Given an array of unsorted numbers and a target sum, count all triplets in it
# such that arr[i] + arr[j] + arr[k] where i, j, k are three different indices.
# Write a function to return the count of such triplets

# Solution:
# 1. Sort the array, then iterate through it
# If we are at number 'X', we need to find 'Y' and 'Z' such that
# X + Y + Z < target. The problem translates into finding a pair whose sum is
# less than 'target - X' (as from the above equation Y + Z == target - X).
# we can find a similar approach as discussed in Triplet sum to zero

def triplet_with_smaller_sum(arr, target):
    arr.sort()
    count = 0
    for i in range(len(arr) - 2):
        count += search_pair(arr, target-arr[i], i)
    return count

def search_pair(arr, target_sum, first):
    count = 0
    left, right = first + 1, len(arr)-1

    while (left < right):
        # find pair whose sum Y + Z is less than target_sum (i.e. target-arr[i])
        if arr[left] + arr[right] < target_sum: # found the triplet
        # since arr[right] >= arr[left], therefore, we can replace arr[right] by
        # any number between left and right to get a sum less than target sum
            count += right - left
            left += 1
        else:
            right -= 1 # we need a pair with a smaller sum
    return count

def main():
  print(triplet_with_smaller_sum([-1, 0, 2, 3], 3))
  print(triplet_with_smaller_sum([-1, 4, 2, 1, 3], 5))


main()
