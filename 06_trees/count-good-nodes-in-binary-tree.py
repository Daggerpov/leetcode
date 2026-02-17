# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# good(x): path from root to node (x) contains no nodes with val greater than x

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node, maxVal):
            if not node:
                return 0 # no good nodes from within this subtree

            if node.val >= maxVal:
                # we're good to keep searching
                # this is a good node
                num_good_nodes = 1
            else:
                num_good_nodes = 0

            maxVal = max(maxVal, node.val) # possibly over-write maxVal

            num_good_nodes += dfs(node.left, maxVal)
            num_good_nodes += dfs(node.right, maxVal)

            return num_good_nodes

        return dfs(root, root.val)

        dfs(root) # root = 2
