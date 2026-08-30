"""102. Binary Tree Level Order Traversal

https://leetcode.com/problems/binary-tree-level-order-traversal/
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
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        nodeQueue = deque([root])
        ans = []

        while nodeQueue:
            numberOfNodesLevel = len(nodeQueue)
            # list to store node values by level
            valuesByLevel = []

            for i in range(numberOfNodesLevel):
                firstNode = nodeQueue.popleft()
                # if the node is not None, append the value to list
                if firstNode:
                    valuesByLevel.append(firstNode.val)

                    # append the children of the node to deque
                    nodeQueue.append(firstNode.left)
                    nodeQueue.append(firstNode.right)

            # append values of the level to List[List]
            if valuesByLevel:
                ans.append(valuesByLevel)

        # return List[List]
        return ans
