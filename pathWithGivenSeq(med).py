# Path with a given sequence (medium)

# Given a binary tree and a number sequence, find if the sequence is present as a
# root-to-leaf path in the given tree.

# Solution: We can follow the same DFS approach and additionally, track the element
# of the given sequence that we should match with the current node. Also, we can return
# false as soon as we find a mismatch between the sequence and the node value.

# The time complexity of the above algorithm is O(N)
# , where ‘N’ is the total number of nodes in the tree.
# This is due to the fact that we traverse each node once.

class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def find_path(root, sequence):
  # TODO: Write your code here
  if not root:
      return len(sequence) == 0 # False
  return find_path_recursive(root, sequence, 0)

def find_path_recursive(currentNode, sequence, sequenceIndex):
    if currentNode is None:
        return False

    seqLen = len(sequence)
    # return False if index out of bounds, or currentNode.val not equal to sequence at particular sequence index
    if currentNode.val != sequence[sequenceIndex] or sequenceIndex >= seqLen:
        return False

    # if the current node is a leaf, and it is the end of a sequence, we have found a path!!
    if currentNode.left is None and currentNode.right is None and sequenceIndex == seqLen - 1:
        return True

    # recursively call to traverse the left and right sub-tree
    # return True if any of the two recursive call return true
    return find_path_recursive(currentNode.left, sequence, sequenceIndex + 1) or \
            find_path_recursive(currentNode.right, sequence, sequenceIndex + 1)

def main():

  root = TreeNode(1)
  root.left = TreeNode(0)
  root.right = TreeNode(1)
  root.left.left = TreeNode(1)
  root.right.left = TreeNode(6)
  root.right.right = TreeNode(5)

  print("Tree has path sequence: " + str(find_path(root, [1, 0, 7])))
  print("Tree has path sequence: " + str(find_path(root, [1, 1, 6])))


main()
