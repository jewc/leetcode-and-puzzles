# Cyclic sort
# Problem Statement#
# We are given an array containing n objects. Each object, when created,
# was assigned a unique number from the range 1 to n based on their creation sequence.
# This means that the object with sequence number 3 was created just before the object with sequence number 4.

# Write a function to sort the objects in-place on their creation sequence number in O(n)
# and without using any extra space. For simplicity, let’s assume we are passed an
# integer array containing only the sequence numbers, though each number is actually an object.

# Time complexity#
# The time complexity of the above algorithm is O(n).
# Although we are not incrementing the index i when swapping the numbers, this will
# result in more than n iterations of the loop, but in the worst-case scenario,
# the while loop will swap a total of n-1 numbers, and once a number is at its
# correct index, we will move on to the next number by incrementing i.
# So overall, our algorithm will take O(n) + O(n-1)
#  which is asymptotically equivalent to O(n).
#
# Space complexity#
# The algorithm runs in constant space O(1)

def cyclic_sort(nums):
    i = 0
    while i < len(nums):

        j = nums[i] - 1 # j is index from 0 to len(nums) - 1

        #print("j: " + str(j))
        #print("i: " + str(i))
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1
    return nums

def main():
  print(cyclic_sort([1, 3, 5, 4, 2]))
  #print(cyclic_sort([3, 1, 5, 4, 2]))
  #print(cyclic_sort([2, 6, 4, 3, 1, 5]))
  # print(cyclic_sort([1, 5, 6, 4, 3, 2]))


main()
