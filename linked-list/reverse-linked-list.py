# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head:
            temp_next = head.next
            head.next = prev
            prev = head
            head = temp_next

        return prev

# Alternative solution:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverseNode(node, prev):
            if not node:
                return prev

            next = node.next
            node.next = prev

            return reverseNode(next, node)

        return reverseNode(head, None)
