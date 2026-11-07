
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        # Base case
        if not root:
            return 0

        # Find left and right subtree depth
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        # Return maximum depth
        return 1 + max(left_depth, right_depth)


# Main Program
# Create a binary tree:
#        3
#       / \
#      9   20
#          / \
#         15  7

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

solution = Solution()
result = solution.maxDepth(root)

print("Maximum Depth:", result)
