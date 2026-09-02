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
            # print("-while")
            # print(f"resCurr: {resCurr.val}, curr1: {curr1.val}, curr2: {curr2.val}")
            # print(f"resCurr.next: {resCurr.next.val}")
            if curr1 and curr2:
                if curr1.val <= curr2.val:
                    # print("curr1 is less")
                    resCurr.next = curr1
                    # if resCurr.next: print(f"resCurr.next is chenged to {resCurr.next.val}")
                    curr1 = curr1.next
                    # if curr1: print(f"curr1 is changed to {curr1.val}")
                else:
                    # print("curr2 is less")
                    resCurr.next = curr2
                    # if resCurr.next: print(f"resCurr.next is chenged to {resCurr.next.val}")
                    curr2 = curr2.next
                    # if curr2: print(f"curr2 is changed to {curr2.val}")
                resCurr = resCurr.next
                # print(f"resCurr is changed to {resCurr.val}")
            else:
                if not curr1:
                    resCurr.next = curr2
                    curr2 = curr2.next
                elif not curr2:
                    resCurr.next = curr1
                    curr1 = curr1.next
                resCurr = resCurr.next
            # print(f"now resCurr: {resCurr.val}, curr1: {curr1.val}, curr2: {curr2.val}")
            print()

        return head
