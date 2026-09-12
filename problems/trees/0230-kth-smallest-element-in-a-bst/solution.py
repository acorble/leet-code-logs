"""230. Kth Smallest Element in a BST

https://leetcode.com/problems/kth-smallest-element-in-a-bst/
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        vals = []

        def dfs(node: Optional[TreeNode]):
            if not node:
                return

            nonlocal vals
            vals.append(node.val)

            dfs(node.left)
            dfs(node.right)

            return

        dfs(root)
        # return the last element which is k th smallest value
        vals.sort()
        return vals[k - 1]
