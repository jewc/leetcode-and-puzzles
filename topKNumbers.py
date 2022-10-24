# Top 'K' numbers (easy)

# Given an unsorted array of numbers, find Kth smallest number in it.
# Please note that it is the Kth smallest number in the sorted order, not the Kth distinct element.

from heapq import *

def find_Kth_smallest_number(nums, k):
  # TODO: Write your code here
  maxHeap = []
  # put first k numbers in the max heap
  for i in range(k):
      heappush(maxHeap, -nums[i])
  # go through the remaining numbers of the array, if the number from the array is smaller
  # then the top (largest) number of the heap, remove the top number from the heap
  # and add the number from the array

  for i in range(k, len(nums)):
      if -nums[i] > maxHeap[0]:
          heappop(maxHeap) # heapq.heappop(heap). Pop and return the smallest item from the heap, maintaining the heap invariant.
          heappush(maxHeap, -nums[i]) # heapq.heappush(heap, item)¶ Push the value item onto the heap, maintaining the heap invariant.

  # root of the heap has the Kth smallest number
  return -maxHeap[0]

def main():

  print("Kth smallest number is: " +
        str(find_Kth_smallest_number([1, 5, 12, 2, 11, 5], 3)))

  # since there are two 5s in the input array, our 3rd and 4th smallest numbers should be a '5'
  print("Kth smallest number is: " +
        str(find_Kth_smallest_number([1, 5, 12, 2, 11, 5], 4)))

  print("Kth smallest number is: " +
        str(find_Kth_smallest_number([5, 12, 11, -1, 12], 3)))


main()
