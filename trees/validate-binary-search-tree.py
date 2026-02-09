# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # recursively call some function on root's children to determine
        # if they're also valid BSTs

        def isSubTreeValidBST(root, left, right):
            if not root:
                return True
            if not (left < root.val and right > root.val):
                return False

            return isSubTreeValidBST(root.left, left, root.val) and isSubTreeValidBST(root.right, root.val, right)

        return isSubTreeValidBST(root, float("-inf"), float("inf"))
