# Count Paths for a Sum (med)
# Given a binary tree and a number ‘S’, find all paths in the tree such that the
# sum of all the node values of each path equals ‘S’. Please note that the paths
# can start or end at any node but all paths must follow direction from parent to child (top to bottom).

# Solution: This problem follows the Binary Tree Path Sum pattern. We can follow the same DFS approach. But there will be four differences:

# 1. Track the current path in a list which will be passed to every recursive call

# 2. Whenever we traverse a node we will do the two things
# Add the current node to the current path
# As we added a new node to the current path, we should find the sums of all sub-paths
# ending at the current node. If the sum of any sub-path is equal to 'S' we increment our path count

# 3. We will traverse all pats and will not stop processing after finding the first path

# 4. Remove the current node from the path before returning the function. This is needed to backtrack while
# we are going up the recursive call stack to process other paths


class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def count_paths(root, S):
  # TODO: Write your code here
  return count_paths_recursive(root, S, [])

def count_paths_recursive(currentNode, S, currentPath):
    if currentNode is None:
        return 0

    # add current node to the path
    currentPath.append(currentNode.val)
    pathCount, pathSum = 0, 0

    # for loop to find the sub-paths
    # find the sums of all sub-paths in the current path list
    for i in range(len(currentPath)-1,-1,-1):
        pathSum += currentPath[i]

        # if the sum of any sub-path is equal to 'S' we increment our path count
        if S == pathSum:
            pathCount += 1

    # traverse the left sub-tree, right sub-tree
    pathCount += count_paths_recursive(currentNode.left, S, currentPath)
    pathCount += count_paths_recursive(currentNode.right, S, currentPath)

    # Remove the current node from path to backtrack
    # need to remove the current node while we are going up the recursive call stack
    del currentPath[-1]

    return pathCount

def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(4)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Tree has paths: " + str(count_paths(root, 11)))


main()
