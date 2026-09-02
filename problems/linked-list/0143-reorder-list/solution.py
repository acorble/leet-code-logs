"""143. Reorder List

https://leetcode.com/problems/reorder-list/
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        nodeList = []
        curr = head

        while curr:
            nodeList.append(curr)
            curr = curr.next

        i = 0
        e = len(nodeList) - 1
        while i < e - i:
            nodeList[i].next = nodeList[e - i]
            nodeList[e - i].next = None
            if (e - i) - i > 1:
                nodeList[e - i].next = nodeList[i + 1]
                nodeList[i + 1].next = None
            i += 1
