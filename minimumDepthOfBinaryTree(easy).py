# Minimum depth of a binary tree (easy)

# PS: Find the minimum depth of a binary tree. The minimum depth is the number of nodes along the shortest path from the root node to the nearest leaf node.

# Solution: This problem follows the Binary Tree Level Order Traversal pattern.
# We can follow the same BFS approach. The only difference will be,
# instead of keeping track of all the nodes in a level, we will only track the depth of the tree.
# As soon as we find our first leaf node, that level will represent the minimum depth of the tree.

from collections import deque


class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None


def find_minimum_depth(root):
  # TODO: Write your code here

  if root is None:
      return 0

  queue = deque()
  queue.append(root)
  min_depth = 0

  while queue:
      min_depth += 1
      levelSize = len(queue)
      # currentLevel = []

      for _ in range(levelSize):
          currentNode = queue.popleft()

          # add the node to the current level
          # currentLevel.append(currentNode.val)

          # check if this node is a leaf node
          if not currentNode.left and not currentNode.right:
              return min_depth

          if currentNode.left:
              queue.append(currentNode.left)
          if currentNode.right:
              queue.append(currentNode.right)


def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Tree Minimum Depth: " + str(find_minimum_depth(root)))
  root.left.left = TreeNode(9)
  root.right.left.left = TreeNode(11)
  print("Tree Minimum Depth: " + str(find_minimum_depth(root)))


main()
