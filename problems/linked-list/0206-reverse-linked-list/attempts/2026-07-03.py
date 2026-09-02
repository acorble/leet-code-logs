"""206. Reverse Linked List

https://leetcode.com/problems/reverse-linked-list/
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        curr = head
        rev = ListNode()

        while curr:
            rev.val = curr.val
            if curr.next is not None:
                new_node = ListNode(curr.next.val)
                new_node.next = rev
                rev = new_node
            curr = curr.next

        return rev


        # brute force
