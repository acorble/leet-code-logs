"""1448. Count Good Nodes in Binary Tree

https://leetcode.com/problems/count-good-nodes-in-binary-tree/
"""

from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # count of good nodes (if exists, increment)
        cnt = 0

        def dfs(X: TreeNode, path: List[int]):
            if not X:
                return

            isGood = True
            nonlocal cnt

            # no nodes that are greater than root from the root of the tree to X
            for n in path:
                if X.val < n:
                    isGood = False
            if isGood:
                cnt += 1

            path.append(X.val)

            # Recursion
            dfs(X.left, path)
            dfs(X.right, path)

            path.pop()

        path = []
        dfs(root, path)

        return cnt
