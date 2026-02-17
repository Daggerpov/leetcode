# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:
            combination = []
            for i in range(0, len(lists), 2):
                if i + 1 < len(lists):
                    combination.append(self.mergeTwoLists(lists[i], lists[i+1]))
                else:
                    combination.append(lists[i])
            lists = combination

        return lists[0]

    def mergeTwoLists(self, l1, l2):
        dummy = ListNode() # will result in O(n) space, where n is total elements in l1 + l2
        combination = dummy

        while l1 and l2:
            if l1.val < l2.val:
                combination.next = l1
                l1 = l1.next
            else:
                # whether l1.val >= l2.val
                combination.next = l2
                l2 = l2.next
            combination = combination.next

        if l1:
            combination.next = l1
        if l2:
            combination.next = l2

        return dummy.next
