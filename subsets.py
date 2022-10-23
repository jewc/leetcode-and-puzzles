# Subsets
#
# Problem Statement
# Given a set with distinct elements, find all of its distinct subsets.
#
#
#
# Time complexity#
# Since, in each step, the number of subsets doubles as we add each element to all
# the existing subsets, therefore, we will have a total of O(2^N) subsets, where
# ‘N’ is the total number of elements in the input set. And since we construct
# a new subset from an existing set, therefore, the time complexity of the above
# algorithm will be O(N*2^N)

#Space complexity#
# All the additional space used by our algorithm is for the output list. Since
# we will have a total of O(2^N).
# subsets, and each subset can take up to O(N) space, therefore, the space
# complexity of our algorithm will be O(N*2^N)

def find_subsets(nums):
  subsets = []
  # start by adding the empty set
  subsets.append([])

  for currentNumber in nums:
      # we will take all existing subsets and insert current number in them to
      # create new subsets
      n = len(subsets)
      for i in range(n):
          # create a new subset from existing subset and insert the current
          # element to it
          set1 = list(subsets[i])
          set1.append(currentNumber)
          subsets.append(set1)

  return subsets


def main():

  print("Here is the list of subsets: " + str(find_subsets([1, 3])))
  print("Here is the list of subsets: " + str(find_subsets([1, 5, 3])))


main()
