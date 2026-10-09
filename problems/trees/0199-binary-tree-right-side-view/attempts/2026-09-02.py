"""199. Binary Tree Right Side View

https://leetcode.com/problems/binary-tree-right-side-view/
"""

from collections import deque
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque([root])
        ret = []

        if not root:
            return []

        while q:
            node = None
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            # append to ret here
            ret.append(node.val)

        return ret
