"""98. Validate Binary Search Tree

https://leetcode.com/problems/validate-binary-search-tree/
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root: TreeNode):
            if not root:
                return True, None, None

            isBSTLeft, minValLeft, maxValLeft = dfs(root.left)
            isBSTRight, minValRight, maxValRight = dfs(root.right)

            minEver = minValLeft if minValLeft is not None else root.val
            maxEver = maxValRight if maxValRight is not None else root.val

            if isBSTLeft and isBSTRight and (maxValLeft is None or maxValLeft < root.val) and (minValRight is None or root.val < minValRight):
                return True, minEver, maxEver
            else:
                return False, minEver, maxEver

        isBST, *_ = dfs(root)

        return isBST
