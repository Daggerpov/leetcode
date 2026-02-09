# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find middle
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # at this point, slow will be at the middle node
        # if the list has even number of nodes -> it'll be at the smaller index

        # -> e.g. if middle is between nodes 2 & 3 -> `slow` will be at 2
        second = slow.next
        prev = slow.next = None

        # reverse 2nd half of list
        while second:
            # reverse the links

            # e.g. if have nodes 2 -> 3 -> 4
            # slow is at node 2
            temp = second.next # node 4
            second.next = prev # node 3 points to None now
            # 2 -> 3, None <- 3, 4
            prev =  second # prev is 3 now
            second =  temp

        # merge lists (taking nodes from 1st & 2nd halves repeatedly)
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
