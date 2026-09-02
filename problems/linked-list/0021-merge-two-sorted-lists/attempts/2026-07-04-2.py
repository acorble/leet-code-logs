"""21. Merge Two Sorted Lists

https://leetcode.com/problems/merge-two-sorted-lists/
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1: return list2
        if not list2: return list1

        curr1, curr2 = list1, list2
        head = None
        resCurr = None

        # define initial current node
        if curr1.val <= curr2.val:
            resCurr = curr1
            curr1 = curr1.next
        else:
            resCurr = curr2
            curr2 = curr2.next

        head = resCurr

        while curr1 or curr2:
            if curr1 and curr2:
                if curr1.val <= curr2.val:
                    resCurr.next = curr1
                    curr1 = curr1.next
                else:
                    resCurr.next = curr2
                    curr2 = curr2.next
                resCurr = resCurr.next
            else:
                if not curr1:
                    resCurr.next = curr2
                    curr2 = curr2.next
                elif not curr2:
                    resCurr.next = curr1
                    curr1 = curr1.next
                resCurr = resCurr.next

        return head
