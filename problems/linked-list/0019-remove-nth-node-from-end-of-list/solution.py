"""19. Remove Nth Node From End of List

https://leetcode.com/problems/remove-nth-node-from-end-of-list/
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        # set up dummy node
        dummy = ListNode(-1, head)

        curr = dummy
        for _ in range(n + 1):
            curr = curr.next

        fast = curr
        slow = dummy

        while fast:
            slow = slow.next
            fast = fast.next

        # remove the next node of slow position
        slow.next = slow.next.next

        return dummy.next
