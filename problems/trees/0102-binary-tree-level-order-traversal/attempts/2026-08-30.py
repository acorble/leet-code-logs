"""102. Binary Tree Level Order Traversal

https://leetcode.com/problems/binary-tree-level-order-traversal/
"""

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        stack = [root]
        # define List[List] as the answer to return
        ans = []

        while stack:
            # define a list to store node values level by level
            listByLevel = []
            numberOfNodes = len(stack)
            for i in range(numberOfNodes):
                # append the node.val to the list
                listByLevel.append(stack[0].val)

                # append the children of the node to stack if not None
                if stack[0].left:
                    stack.append(stack[0].left)
                if stack[0].right:
                    stack.append(stack[0].right)

                # remove the node from the stack
                stack.pop(0)
            # append the list to List[List]
            ans.append(listByLevel)

        return ans
