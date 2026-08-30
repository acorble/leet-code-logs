"""543. Diameter of Binary Tree

https://leetcode.com/problems/diameter-of-binary-tree/
"""

from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        maxLength = 0

        # traverse all nodes
        while queue:
            curr = queue.popleft()
            # for each node
            # compute the depth of left subtree
            leftDepth = self.maxOfDepth(curr.left)
            # also right tree
            rightDepth = self.maxOfDepth(curr.right)
            # compute the max length with current node and update max
            Length = leftDepth + rightDepth
            maxLength = max(maxLength, Length)

            # append children to queue
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)

        return maxLength

    def maxOfDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return max(self.maxOfDepth(root.left), self.maxOfDepth(root.right)) + 1
