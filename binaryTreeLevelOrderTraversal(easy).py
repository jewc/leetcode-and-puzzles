# Given a binary tree, populate an array to represent its level-by-level traversal.
# You should populate the values of all nodes of each level from left to right in separate sub-arrays.

# Use Breadth First Search to traverse all nodes of each level, before moving onto the next level.
# Here are the steps of our algorithm

# Use a queue to efficiently traverse in BFS fashion. Here are the steps of our algorithm

# 1. Start by pushing the root node to the queue
# 2. Keep iterating until the queue is empty
# 3. In each iteration, first count the elements in the queue (let's call it levelSize).
#   We will have these many nodes in the current level
# 4. Next, remove levelSize nodes from the queue and push their value in an array to represent the current level
# 5. After removing each node from the queue, insert both of its children into the queue.
# 6. If the queue is not empty. repeat from step 3 for the next level

# time complexity
# The time complexity of the above algorithm is O(N), where āNā is the total
# number of nodes in the tree. This is due to the fact that we traverse each node once.

from collections import deque


class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None


def traverse(root):
  result = []
  if root is None:
    return result

  queue = deque()
  # add root to the queue
  queue.append(root)
  while queue:
      levelSize = len(queue)
      currentLevel = []

      for _ in range(levelSize):
          # pop the leftmost element from the queue
          currentNode = queue.popleft()

          # add the node to the current level
          currentLevel.append(currentNode.val)

          # push/insert the children of current node in the queue
          if currentNode.left:
              queue.append(currentNode.left)
          if currentNode.right:
              queue.append(currentNode.right)

        # move element to the output array
      result.append(currentLevel)

  return result


def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Level order traversal: " + str(traverse(root)))


main()
