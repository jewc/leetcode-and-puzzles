# Given a string, find the length of the longest substring in it
# with no more than K distinct characters.

def longest_substring_with_k_distinct(str1, k):
    window_start = 0
    max_length = 0
    char_frequency = {} # hashmap to store count of characters

    # extend range of [window_start, window_end]
    for window_end in range(len(str1)):
        right_char = str1[window_end]

        #update hashmap
        if right_char not in char_frequency:
            char_frequency[right_char] = 0
        char_frequency[right_char] += 1

        # try to shrink the window from the beginning if the count of unique
        # characters in the hashmap is greater than k
        while len(char_frequency) > k:
            left_char = str1[window_start] # update left char with window_start
            char_frequency[left_char] -= 1 # decrement frequency of left_char
            if char_frequency[left_char] == 0: del char_frequency[left_char]
            window_start += 1

    max_length = max(max_length, window_end - window_start + 1)

    return max_length

def main():
  print("Length of the longest substring: " + str(longest_substring_with_k_distinct("araaci", 2)))
  print("Length of the longest substring: " + str(longest_substring_with_k_distinct("araaci", 1)))
  print("Length of the longest substring: " + str(longest_substring_with_k_distinct("cbbebi", 3)))
  print("Length of the longest substring: " + str(longest_substring_with_k_distinct("cbbebiiiii", 3)))


main()
