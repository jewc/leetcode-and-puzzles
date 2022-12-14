# insert interval
# medium
#
# Problem Statement #
# Given a list of non-overlapping intervals sorted by their start time, insert a
# given interval at the correct position and merge all necessary intervals to
# produce a list that has only mutually exclusive intervals.


# Time complexity#
# As we are iterating through all the intervals only once, the time complexity
# of the above algorithm is O(N), where āNā is the total number of intervals.
#
# Space complexity#
# The space complexity of the above algorithm will be O(N)
#  as we need to return a list containing all the merged intervals.

def insert(intervals, new_interval):
  merged = []
  i = 0
  start = 0
  end = 1

  # skip (and add to output) all intervals that come before the 'new_interval'
  while i < len(intervals) and intervals[i][end] < new_interval[start]:
      merged.append(intervals[i])
      i += 1

  # merge all intervals that overlap with 'new_interval'
  while i < len(intervals) and intervals[i][start] <= new_interval[end]:
      new_interval[start] = min(intervals[i][start], new_interval[start])
      new_interval[end] = max(intervals[i][end], new_interval[end])
      i += 1

  # insert the new interval
  merged.append(new_interval)

# add all remaining intervals to the output
  while i < len(intervals):
      merged.append(intervals[i])
      i += 1

  return merged


def main():
  print("Intervals after inserting the new interval: " + str(insert([[1, 3], [5, 7], [8, 12]], [4, 6])))
  print("Intervals after inserting the new interval: " + str(insert([[1, 3], [5, 7], [8, 12]], [4, 10])))
  print("Intervals after inserting the new interval: " + str(insert([[2, 3], [5, 7]], [1, 4])))


main()
