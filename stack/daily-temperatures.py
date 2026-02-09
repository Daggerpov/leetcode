"""
Maintain a monotonic (l->r) decreasing stack with a temperature and its index in an array, or tuple. As going through temperatures, if it's greater than the last elem of stack, pop that elem and mark the difference between curIndex and the index it was placed in stack with (num days it took to get warmer temperature) in the resulting array of day diffs -> crucial: keep traversing stack right->left doing this until cur element is greater than or equal to last element of stack. In which case, just append to stack with index.
"""
