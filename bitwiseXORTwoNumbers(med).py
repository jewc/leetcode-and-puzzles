# bitwise xor
# Two Single Numbers (medium)
# Problem Statement#
# In a non-empty array of numbers, every number appears exactly twice except two
# numbers that appear only once. Find the two numbers that appear only once.

# Time Complexity#
# The time complexity of this solution is O(n) where ‘n’ is the number of elements in the input array.

# Space Complexity#
# The algorithm runs in constant space O(1).

def find_single_numbers(nums):
  # get the XOR for all the Numbers
  n1xn2 = 0
  for num in nums:
      n1xn2 ^= num

  # get the rightmost bit that is '1'
  rightmost_set_bit = 1
  while (n1xn2 & rightmost_set_bit) == 0:
      rightmost_set_bit = rightmost_set_bit << 1
  num1, num2 = 0, 0

  for num in nums:
      if (num & rightmost_set_bit) != 0: # the bit is set
        num1 ^= num
      else: # the bit is not set
        num2 ^= num

  return [num1, num2]


def main():
  print('Single numbers are:' +
        str(find_single_numbers([1, 4, 2, 1, 3, 5, 6, 2, 3, 5])))
  print('Single numbers are:' + str(find_single_numbers([2, 1, 3, 2])))

main()