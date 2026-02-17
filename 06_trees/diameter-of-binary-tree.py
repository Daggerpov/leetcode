# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxDiam = 0

        def maxDepth(node):
            if not node: return 0

            # get max depth of left + right subtrees
            # add together
            # see if that's > self.maxDiam -> overwrite self.maxDiam if so

            leftDepth = maxDepth(node.left) #2's left depth: 2
            rightDepth = maxDepth(node.right) # 2's right depth: 1

            curDiam = leftDepth + rightDepth # + 2 + 1

            self.maxDiam = max(self.maxDiam, curDiam)

            return 1 + max(leftDepth, rightDepth)


        maxDepth(root)

        return self.maxDiam

# Alternative solution (Iterative DFS to save call stack memory):

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        stack = [root]
        mp = {None: (0, 0)}

        while stack:
            node = stack[-1]

            if node.left and node.left not in mp:
                stack.append(node.left)
            elif node.right and node.right not in mp:
                stack.append(node.right)
            else:
                node = stack.pop()

                leftHeight, leftDiameter = mp[node.left]
                rightHeight, rightDiameter = mp[node.right]

                mp[node] = (1 + max(leftHeight, rightHeight),
                           max(leftHeight + rightHeight, leftDiameter, rightDiameter))

        return mp[root][1]
