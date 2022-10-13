# Pair with target sum

# Time Complexity#
# The time complexity of the above algorithm will be O(N),
# where ‘N’ is the total number of elements in the given array.
#
# Space Complexity#
# The algorithm runs in constant space O(1).
# Easy

def pair_with_targetsum(arr, target_sum):
    left = 0
    right = len(arr) - 1

    while (left<right):
        current_sum = arr[left] + arr[right]

        if current_sum == target_sum:
            return [left, right]

        if target_sum > current_sum:
            left += 1 # we need a pair with a larger sum
        else:
            right -= 1

    return [-1,-1]

# alternate approach

# Time Complexity#
# The time complexity of the above algorithm will be O(N),
# where ‘N’ is the total number of elements in the given array.
#
# Space Complexity#
# The space complexity will also be O(N), as, in the worst case,
# we will be pushing ‘N’ numbers in the HashTable.

def_pair_with_target_sum_alt(arr, target_sum):
    hash_table = {} # to store numbers and their indices
    for i, num in enumerate(arr):

        # Suppose "X+Y == target_sum"
        # search for 'Y', which is equivalent to
        # 'Target - X'
        if target_sum - num in hash_table:

            # if Y exists, then we have found the required pair
            return [nums[target_sum - num], i]
        else:
            # insert 'X' into hash table
            nums[arr[i]] = i
        return [-1,-1]


def main():
  print(pair_with_targetsum([1, 2, 3, 4, 6], 6))
  print(pair_with_targetsum([2, 5, 9, 11], 11))


main()
