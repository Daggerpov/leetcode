"""
- Create a deque to traverse all nodes in a BFS manner from the root
- Go through all nodes, storing them into a hashmap with keys of columns
    - Appropriately mark column based on popped node from deque
    - Appropriately mark row based on the current BFS level, or from popped node
- Sort the hashmap based on the keys by for i in sorted(columnsHashMap.keys())
- Append to the res array the sorted nodes of that column's node values
"""
