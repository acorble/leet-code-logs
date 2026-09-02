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
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # now fast reached the end, slow is in middle of linked-list
        # cut connection between slow and slow.next
        headSecond = slow.next
        slow.next = None

        # reverse second half of linked list
        prev = None
        while headSecond:
            tmp = headSecond.next
            headSecond.next = prev
            prev = headSecond
            headSecond = tmp

        # first half :head, second half: prev
        while head and prev:
            headNext = head.next
            prevNext = prev.next

            # update link
            head.next = prev
            prev.next = headNext

            head = headNext
            prev = prevNext
