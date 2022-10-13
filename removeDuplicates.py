# Remove duplicates
# Given an array of sorted numbers, remove all duplicate number instances from
# it in-place, such that each element appears only once. The relative order of
# the elements should be kept the same and you should not use any extra space
# so that that the solution have a space complexity of O(1).

# Move all the unique elements at the beginning of the array and after moving
# return the length of the subarray that has no duplicate in it.

# Time Complexity#
# The time complexity of the above algorithm will be O(N),
# where ‘N’ is the total number of elements in the given array.
#
# Space Complexity#
# The algorithm runs in constant space O(1).

def remove_duplicates(arr):
    # index of next non-duplicate element
    next_non_duplicate = 1

    i = 0
    # shift elements left whenever we encounter duplicates
    while (i < len (arr)):

        # increment next_non_duplicate if
        # next_non duplicate is not ahead of next (i.e. not in base case)
        if (arr[next_non_duplicate - 1] != arr[i]):
            # replace value at index next_non_duplicate with value index next
            arr[next_non_duplicate] = arr[i]
            next_non_duplicate += 1
        i += 1
    return next_non_duplicate

def main():
  print(remove_duplicates([2, 3, 3, 3, 6, 9, 9]))
  print(remove_duplicates([2, 2, 2, 11]))


main()
