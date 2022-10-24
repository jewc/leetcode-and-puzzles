# happy number
# Any number will be called a happy number if, after repeatedly replacing it with
# a number equal to the sum of the square of all of its digits, leads us to number ‘1’.
# All other (not-happy) numbers will never reach ‘1’. Instead, they will be stuck in a
# cycle of numbers which does not include ‘1’.

# e.g. 23 - a happy number
# 2^2 + 3^2 = 4 + 9 = 13
# 1^2 + 3^2 = 1 + 9 = 10
# 1^2 + 0^2 = 1 + 0 = 1

# e.g. 12 - not a happy numbers
# 1^2 + 2^2 = 5
# 5^2 = 25
# 2^2 + 5^2 = 4 + 25 = 29
# 2^2 + 9^2 = 4 + 81 = 85
# 8^2 + 5^2 = 64 + 25 = 89
# ...
# 3^2 + 7^2 = 9 + 49 = 58
# 5^2 + 8^2 = 25 + 64 = 89


# solution
# The process, defined above, to find out if a number is a happy number or not,
# always ends in a cycle.
# If the number is a happy number, the process will be stuck in a cycle on number ‘1,’
#  and if the number is not a happy number then the process will be stuck in a cycle
#  with a set of numbers. As we saw in Example-2 while determining if ‘12’ is a
#  happy number or not, our process will get stuck in a cycle with the following
#  numbers: 89 -> 145 -> 42 -> 20 -> 4 -> 16 -> 37 -> 58 -> 89

# Time Complexity


def find_happy_number(num):
  # TODO: Write your code here
  slow, fast = num, num

  while True:
      slow = find_square_sum(slow) # move one step
      fast = find_square_sum(find_square_sum(fast)) # move two steps
      if slow == fast: # found the cycle
        break
  return slow == 1 # see if the cycle is stuck on the number 1! Then it is a happy number

def find_square_sum(num):
    _sum = 0
    while (num > 0):
        digit = num % 10
        _sum += digit * digit
        num //= 10
    return _sum

def main():
  print(find_happy_number(23))
  print(find_happy_number(12))


main()
