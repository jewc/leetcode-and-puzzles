# Given a string, find the length of the longest substring, which has all distinct characters.
# hard


# The above algorithm’s time complexity will be O(N),
# where ‘N’ is the number of characters in the input string.
#
# The algorithm’s space complexity will be O(K) , where K
# is the number of distinct characters in the input string. This also means K<=N
#, because in the worst case, the whole string might not have any
# duplicate character, so the entire string will be added to the HashMap.
# Having said that, since we can expect a fixed set of characters in the input
# string (e.g., 26 for English letters), we can say that the algorithm runs in
# fixed space O(1) ; in this case, we can use a fixed-size array instead of
# the HashMap.

def non_repeat_substring(str):
    window_start = 0
    max_length = 0
    char_index_map = {}

    # extend the range [window_start, window_end]
    for window_end in range(len(str)):
        right_char = str[window_end]

        # if the map already contains the 'right_char',
        # shrink the window from beginning so that
        # we have only one occurrence of 'right_char'

        if right_char in char_index_map:
            # in the current window,
            # we will not have any 'right_char' after its previous index
            # and if 'window_start' is already ahead of the last index of
            # 'right_char', we'll keep 'window_start'
            window_start = max(window_start, char_index_map[right_char] + 1)

        # insert the 'right_char' into the char_index_map
        char_index_map[right_char] = window_end

        # get the maximum so far
        max_length = max(max_length, window_end - window_start + 1)
    return max_length

def main():
  print("Length of the longest substring: " + str(non_repeat_substring("aabccbb")))
  print("Length of the longest substring: " + str(non_repeat_substring("abbbb")))
  print("Length of the longest substring: " + str(non_repeat_substring("abccde")))
  print("Length of the longest substring: " + str(non_repeat_substring("abccd")))

main()
