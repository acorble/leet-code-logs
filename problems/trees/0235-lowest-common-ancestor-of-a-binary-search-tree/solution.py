"""235. Lowest Common Ancestor of a Binary Search Tree

https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode'):
            if not root:
                return False, False, None

            isPFoundLeft, isQFoundLeft, lcaLeft = dfs(root.left, p, q)
            isPFoundRight, isQFoundRight, lcaRight = dfs(root.right, p, q)

            isPFound = isPFoundLeft or isPFoundRight
            isQFound = isQFoundLeft or isQFoundRight

            if not isPFound and root.val == p.val:
                isPFound = True

            if not isQFound and root.val == q.val:
                isQFound = True

            lca = None

            if lcaLeft:
                lca = lcaLeft
            elif lcaRight:
                lca = lcaRight
            else:
                if isPFound and isQFound:
                    lca = root

            return isPFound, isQFound, lca

        # search for p and q
        _, _, lca = dfs(root, p, q)
        return lca
