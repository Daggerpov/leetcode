# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # ! will need to implement BFS
        # ! will use a queue to do so, rather than doing it recursively

        # deque = double-ended queue
        q = deque() # will pop elements from this queue's left side
        total_results = []

        if root:
            q.append(root)

        while q:
            level_results = []

            for i in range(len(q)): # 1 to start off, then len of children, etc.
                cur_element = q.popleft()
                if cur_element: # because it could be None
                    level_results.append(cur_element.val)
                    if cur_element.left:
                        q.append(cur_element.left)
                    if cur_element.right:
                        q.append(cur_element.right)
                # don't want to break in the `else` case, since it's not necessarily
                # a complete binary tree -> meaning there could be `None` `TreeNode`s
                # between valid ones that I still should search for afterwards in that level
            total_results.append(level_results)

        return total_results
