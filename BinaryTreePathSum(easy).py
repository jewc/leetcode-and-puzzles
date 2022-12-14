# Depth First Search
# Binary Tree Path Sum(easy)

# Given a binary tree and a number āSā, find if the tree has a path from root-to-leaf
# such that the sum of all the node values of that path equals āSā.

# time complexity
# O(N), where N is the total number of nodes in the tree.
# We traverse each node once

class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def has_path(root, sum):
  # TODO: Write your code here
  if root is None:
      return False
  # if the current node is a leaf and its value is equal to the sum, we've found a path
  if (root.val == sum) and (root.left is None) and (root.right is None):
      return True
  return has_path(root.left, sum - root.val) or has_path(root.right, sum - root.val)

def main():

  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Tree has path: " + str(has_path(root, 23)))
  print("Tree has path: " + str(has_path(root, 16)))


main()
