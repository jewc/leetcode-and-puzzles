# fruits into baskets
# medium

# Time Complexity
# The above algorithm’s time complexity will be O(N)
#, where ‘N’ is the number of characters in the input array.
# The outer for loop runs for all characters, and the inner while loop processes each character only once;
# therefore, the time complexity of the algorithm will be O(N+N)
#, which is asymptotically equivalent to O(N)

# Space Complexity
# The algorithm runs in constant space O(1)
 # as there can be a maximum of three types of fruits stored in the frequency map.


def fruits_into_baskets(fruits):
  window_start = 0
  max_length = 0
  fruit_frequency = {}

  for window_end in range(len(fruits)):
    right_fruit = fruits[window_end]

    # update the hashmap
    if right_fruit not in fruit_frequency:
      fruit_frequency[right_fruit] = 0
    fruit_frequency[right_fruit] +=1

    # two baskets
    while len(fruit_frequency)>2:
      left_fruit = fruits[window_start] # update left fruit with window_start
      fruit_frequency[left_fruit] -= 1 # decrement frequency of left fruit
      if fruit_frequency[left_fruit] == 0: del fruit_frequency[left_fruit]
      window_start += 1

    max_length = max(max_length, window_end - window_start + 1)


  return max_length

def main():
  print("Maximum number of fruits: " + str(fruits_into_baskets(['A', 'B', 'C', 'A', 'C'])))
  print("Maximum number of fruits: " + str(fruits_into_baskets(['A', 'B', 'C', 'B', 'B', 'C'])))


main()
