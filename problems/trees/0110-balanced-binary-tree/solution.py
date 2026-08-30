"""110. Balanced Binary Tree

https://leetcode.com/problems/balanced-binary-tree/
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.isBalancedTotally = True

        maxDepth, isBalanced = self.maxDepthAndIsBalanced(root)

        return self.isBalancedTotally

    def maxDepthAndIsBalanced(self, root: Optional[TreeNode]) -> tuple[int, bool]:
        if not root:
            return 0, True

        leftDepth, isBalancedLeft = self.maxDepthAndIsBalanced(root.left)
        rightDepth, isBalancedRight = self.maxDepthAndIsBalanced(root.right)

        depth = max(leftDepth, rightDepth) + 1

        # compare the depth of subtrees
        if abs(leftDepth - rightDepth) > 1:
            self.isBalancedTotally = False
            return depth, False
        else:
            return depth, True
