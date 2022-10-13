# Given a string with lowercase letters only, if you are allowed to replace
# no more than k letters with any letter,
# find the length of the longest substring having the same letters after replacement.

#Time Complexity#
#The above algorithm’s time complexity will be O(N) ,
#where ‘N’ is the number of letters in the input string.
#
# Space Complexity#
# As we expect only the lower case letters in the input string, we can conclude that the space complexity will be O(26)
#  to store each letter’s frequency in the HashMap, which is asymptotically equal to O(1).

def length_of_longest_substring(str, k):
    window_start = 0
    max_length = 0
    max_repeat_letter_count = 0 # keep track of the count of max repeating letters in any window
    frequency_map = {}

    # Try to extend the range [window_start, window_end]
    for window_end in range(len(str)):
        right_char = str[window_end]
        if right_char not in frequency_map:
            frequency_map[right_char] = 0
        frequency_map[right_char] += 1

        # don't need to place max_repeat_letter_count under the below 'if'
        # keep track of the count of max repeating letter
        max_repeat_letter_count = max(max_repeat_letter_count, frequency_map[right_char])

        # current window size is from window_start to Window_end,
        # overall we have a letter which is  repeating 'max_repeat_letter_count' times.
        #  This mean we can have a window which has one letter repeating
        #  'max_repeat_letter_count' times, and the remaining letters we should replace.
        # if the remaining letters are more than 'k', it is the time to shrink the window
        # as we replace are not allowed to replace more than 'k' letter

        # we don't need to know the exact maximum count of the current window.
        # the only thing we need to know is whether the maximum count exceeds the historical maximum count,
        # and this can only happen because of the newly added char
        if (window_end - window_start + 1 - max_repeat_letter_count) > k:
            left_char = str[window_start]
            frequency_map[left_char] -= 1
            window_start += 1

        max_length = max(max_length, window_end - window_start + 1)

    return max_length

def main():
  print(length_of_longest_substring("aabccbb", 2))
  print(length_of_longest_substring("abbcb", 1))
  print(length_of_longest_substring("abccde", 1))

main()
