"""
BFS, marking the last node at that level, to append it to res
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque([root])
        visibleNodes = []

        while q:
            lastNode = None
            # on current level
            for i in range(len(q)):
                curNode = q.popleft() # left-most node in current level
                if curNode:
                    lastNode = curNode # maybe redundant, TODO: check later
                    q.append(curNode.left)
                    q.append(curNode.right)
            if lastNode:
                visibleNodes.append(lastNode.val)

        return visibleNodes
