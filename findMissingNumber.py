# Find the missing number
# Easy
#
# Problem Statement#
# We are given an array containing n distinct numbers taken from the range 0 to n.
# Since the array has only n numbers out of the total n+1 numbers, find the
# missing number.

# Time complexity#
# The time complexity of the above algorithm is O(n).
# In the while loop, although we are not incrementing the index i when swapping
# the numbers, this will result in more than n iterations of the loop, but in the
# worst-case scenario, the while loop will swap a total of n-1 numbers and once
# a number is at its correct index, we will move on to the next number by
# incrementing i. In the end, we iterate the input array again to find the first
# number missing from its index, so overall, our algorithm will take O(n) + O(n-1) + O(n)
#  which is asymptotically equivalent to O(n).

# Space complexity#
# The algorithm runs in constant space O(1).


# perform cyclic sort
#

def find_missing_number(nums):
  i = 0
  n = len(nums)
  while i < n:
      # j is index from 0 to len(nums)
      j = nums[i]

      print("i: " + str(i) + "; j - : " + str(j))
      # check for index out of bounds, as array indices range from
      # 0 to n-1, not 1 to n

      # to avoid index out of bounds, add conditional if (nums[i] < n)
      if nums[i] < n and nums[i] != nums[j]:
          nums[i], nums[j] = nums[j], nums[i] #swap
      else:
          i += 1

      print (nums)
  # find the first number missing from its index, that will be the required number
  for i in range(n):
      if nums[i] != i:
          return i

  return n


def main():
  print(find_missing_number([4, 0, 3, 1]))
  #print(find_missing_number([8, 3, 5, 2, 4, 6, 0, 1]))


main()
