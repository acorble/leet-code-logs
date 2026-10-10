"""145. Binary Tree Postorder Traversal

https://leetcode.com/problems/binary-tree-postorder-traversal/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: TreeNode | None) -> list[int]:
        ret = []

        def dfs(node):
            if not node:
                return
            nonlocal ret
            dfs(node.left)
            dfs(node.right)

            ret.append(node.val)
            return

        dfs(root)
        return ret
