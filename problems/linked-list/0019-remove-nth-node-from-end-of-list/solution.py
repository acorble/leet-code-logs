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
        # 1回最後まで行きながら番号とノードをhashmapに保存しておいて、最後まで行ききってから特定の番号のノードの前後のrefを更新すればいけえそう
        if not head:
            return None

        # current node to iterate through the list
        curr = head # not None
        # hashmap to store each node and its number
        nodes = {}
        # index number to count the size of the list
        index = 0

        while curr:
            nodes[index] = curr
            index += 1
            curr = curr.next

        # add the last None to nodes map
        nodes[index] = None

        # now index is equal to the size of the list
        if n == index:
            # remove the leftmost node
            return head.next
        else:
            # remove n th node
            nodes[index - n - 1].next = nodes[index - n + 1]
            return head
