# squaring a sorted array
# Easy

# Given a sorted array, create a new array containing squares of all the numbers
# of the input array in the sorted order.

# Time complexity#
# The above algorithm’s time complexity will be O(N)
#  as we are iterating the input array only once.
#
# Space complexity#
# The above algorithm’s space complexity will also be O(N);
# this space will be used for the output array.

def make_squares(arr):
    n = len(arr)

    squares = [0 for x in range(n)] # create array
    highestSquareIdx = n-1

    # have pointers at both ends of the array
    left, right = 0, n-1
    
    while left <= right:
        leftSquare = arr[left] * arr[left]
        rightSquare = arr[right] * arr[right]

        if leftSquare > rightSquare:
            squares[highestSquareIdx] = leftSquare
            left += 1
        else:
            squares[highestSquareIdx] = rightSquare
            right -= 1
        highestSquareIdx -= 1

    return squares

def main():

  print("Squares: " + str(make_squares([-2, -1, 0, 2, 3])))
  print("Squares: " + str(make_squares([-3, -1, 0, 1, 2])))


main()
