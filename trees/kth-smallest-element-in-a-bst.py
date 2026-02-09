# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 0
        self.result = 0
        self.inOrderTraversal(root, k)
        return self.result

    def inOrderTraversal(self, node, k) -> None:
        # Must do in-order traversal
        # -> for each val from in-order traversal, increment a count
        # -> once that count reaches k, return that val since it's the
        # kth smallest element

        if not node or self.count >= k:
            return 0
        # skeleton of in-order traversal, to expand upon with
        # question-specific logic:

        self.inOrderTraversal(node.left, k)
        self.count += 1

        if self.count == k:
            self.result = node.val
            return

        self.inOrderTraversal(node.right, k)

# Alternative solution:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = []

        def dfs(node):
            if not node:
                return

            dfs(node.left)
            arr.append(node.val)
            dfs(node.right)

        dfs(root)
        return arr[k - 1]
