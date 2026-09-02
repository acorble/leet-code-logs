"""141. Linked List Cycle

https://leetcode.com/problems/linked-list-cycle/
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False

        curr = head
        nodeSet = set()

        while curr.next:
            if curr in nodeSet:
                return True
            else:
                nodeSet.add(curr)
                curr = curr.next

        return False
