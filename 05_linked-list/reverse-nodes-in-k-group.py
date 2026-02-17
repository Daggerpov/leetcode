# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head) # val will be 0 by default, as above

        groupPrev = dummy

        while True:
            kthNode = self.getKthNode(groupPrev, k)
            if not kthNode:
                break

            groupNext = kthNode.next # ! don't understand

            cur = groupPrev.next
            prev = kthNode.next

            while cur != groupNext:
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp

            # tricky part:
            temp = groupPrev.next
            groupPrev.next = kthNode # our dummy node points to beginning (kthNode is now start of this group)
            groupPrev = temp # setting new group prev to be new group end node (formerly start node)

        return dummy.next

    def getKthNode(self, node, k):
        kthNode = node
        while k > 0 and kthNode:
            kthNode = kthNode.next
            k -= 1

        return kthNode
