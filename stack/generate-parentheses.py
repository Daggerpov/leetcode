"""
Backtracking: maintain an inner open and closed count. If these ever both reach n, then add to res array. Otherwise, if a closed one can be placed (closedCount < openCount, then increment closedCount and append ")" to string. if openCount < n, then an open can be added.
"""
