"""199. Binary Tree Right Side View

https://leetcode.com/problems/binary-tree-right-side-view/
"""

from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:

        if not root:
            return []
        
        q = deque([root])
        ret = []

        while q:
            node = None
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            # ここでのnodeは層ごとの右端になる
            ret.append(node.val)
        
        return ret
