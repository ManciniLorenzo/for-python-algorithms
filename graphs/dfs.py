"""Depth-first search.

EXTRA: not in the course slides (the slides only use the FIFO version, see
reachability_bfs.py). PLACEHOLDER: not implemented yet.
"""

# --- 1. Problem --------------------------------------------------------------
# Same question as reachability (which nodes can be reached from s?), but
# exploring as deep as possible along one branch before backtracking.

# --- 2. Inputs and outputs ---------------------------------------------------
# TODO: decide:
#   - Input: successor lists and s.
#   - Output: visiting order (a list)? the set of visited nodes? both?

# --- 3. Assumptions and limitations ------------------------------------------
# - Works on directed and undirected graphs.
# - Recursive version: Python's default recursion limit (~1000) breaks on long paths.
# - Visiting order depends on the order of each successor list: several valid outputs exist.

# --- 4. Core idea ------------------------------------------------------------
# Take the reachability algorithm and manage the frontier as a stack (LIFO)
# instead of a queue. Equivalently, recurse: visit u, then recursively visit
# each unvisited successor of u.

# --- 5. Pseudocode -----------------------------------------------------------
# TODO: write pseudocode for BOTH the recursive and the explicit-stack version.
#
#
#

# --- 6. Python concepts to practice -----------------------------------------
# recursion, list as a stack (append / pop), set, default arguments (and why a
# mutable default like `visited=set()` is a classic bug)

# --- 7. Implementation plan --------------------------------------------------
# TODO 1: recursive version with a helper function.
# TODO 2: iterative version with an explicit stack.
# TODO 3: compare the visiting order of the two on the same graph. Are they equal? Why?

# --- 8. Complexity -----------------------------------------------------------
# TODO after implementing: time in terms of n and m? Extra memory of the stack /
# recursion in the worst case? Compare with BFS.

# --- 9. Example to try -------------------------------------------------------
# Reuse the 5-node slide graph from reachability_bfs.py with s = 1. Write the
# BFS order and the DFS order by hand, then check both programs.

# --- 10. Tests and edge cases ------------------------------------------------
# - graph with a cycle (no infinite loop / infinite recursion)
# - a long path of 2000 nodes: what does the recursive version do?
# - same set of visited nodes as reachable_nodes() on several graphs

# --- 11. Self-check questions ------------------------------------------------
# - Exactly which line differs between your BFS and your iterative DFS?
# - Why can two correct DFS implementations print different orders?
# - When would you prefer DFS over BFS?


def dfs_order(graph: dict, s) -> list:
    """Return the nodes reachable from s in depth-first visiting order."""
    raise NotImplementedError("TODO")
