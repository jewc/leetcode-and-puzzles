# connect level order siblings (medium)

# Given a binary tree, connect each node with its level order successor.
# The last node of each level should point to a null node.

from __future__ import print_function
from collections import deque

# solution:
# This problem follows the Binary Tree Level Order Traversal pattern.
# We can follow the same BFS approach. The only difference is that while
# traversing a level we will remember the previous node to connect it with the
# current node.


class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right, self.next = None, None, None

  # level order traversal using 'next' pointer
  def print_level_order(self):
    nextLevelRoot = self
    while nextLevelRoot:
      current = nextLevelRoot
      nextLevelRoot = None
      while current:
        print(str(current.val) + " ", end='')
        if not nextLevelRoot:
          if current.left:
            nextLevelRoot = current.left
          elif current.right:
            nextLevelRoot = current.right
        current = current.next
      print()


def connect_level_order_siblings(root):
  # TODO: Write your code here

  if root is None:
      return None
  queue = deque()
  queue.append(root)

  while queue:
      previousNode = None
      levelSize = len(queue)

      # connect all the nodes at this level
      for _ in range(levelSize):
          currentNode = queue.popleft()
          if previousNode:
              previousNode.next = currentNode
          previousNode = currentNode

          #insert children of current node in the queue
          if currentNode.left:
              queue.append(currentNode.left)
          if currentNode.right:
              queue.append(currentNode.right)

  return

def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  connect_level_order_siblings(root)

  print("Level order traversal using 'next' pointer: ")
  root.print_level_order()


main()
