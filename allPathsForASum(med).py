# All paths for a sum(medium)
# PS: Given a binary tree and a number 'S', find all paths from root to leaf
# such that the sum of all the node values of each path equals 'S'

class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def find_paths(root, sum):
  allPaths = []
  # TODO: Write your code here
  find_paths_recursive(root, sum, [], allPaths)
  return allPaths

def find_paths_recursive(currentNode, required_sum, currentPath, allPaths):
    if currentNode is None:
        return

    # add the current node to the path
    currentPath.append(currentNode.val)

    # if the current node is a leaf and its value is equal to required_sum, save the current path
    if currentNode.val == required_sum and currentNode.left is None and currentNode.right is None:
        allPaths.append(list(currentPath))
    else:
        # traverse the left sub-tree
        find_paths_recursive(currentNode.left, required_sum - currentNode.val, currentPath, allPaths)
        # traverse the right sub-tree
        find_paths_recursive(currentNode.right, required_sum - currentNode.val, currentPath, allPaths)

def main():

  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(4)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  sum = 23
  print("Tree paths with sum " + str(sum) +
        ": " + str(find_paths(root, sum)))


main()
