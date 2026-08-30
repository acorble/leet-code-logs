"""100. Same Tree

https://leetcode.com/problems/same-tree/
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # 両方NoneならTrue
        if not p and not q:
            return True

        # どちらか一方がNoneならFalse
        if not p or not q:
            return False

        # valが違うならFalse
        if p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
