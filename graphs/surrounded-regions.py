"""
Go through every edge cell (by checking index) that is a 0 -> set it to a "T", as well
as all surrounding 0 cells, by recursively calling this dfs in all 4 directions. Then,
go through every cell again, O(m*n), marking all Os that are still Os (should be
captured) as Xs and all T's, back as Os (since they are either O edges, or connected to
0 edges, as shown from DFS neighbouring calls.
"""
