
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        # Base case
        if not root:
            return None

        # Swap left and right children
        root.left, root.right = root.right, root.left

        # Recursively invert left and right subtrees
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root


# Helper function to print tree in level order
def printTree(root):
    if not root:
        return

    queue = [root]

    while queue:
        node = queue.pop(0)
        print(node.val, end=" ")

        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)

    print()


# Main Program
# Original tree:
#        4
#       / \
#      2   7
#     / \ / \
#    1  3 6  9

root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)

solution = Solution()
inverted_root = solution.invertTree(root)

print("Inverted Tree (Level Order):")
printTree(inverted_root)
