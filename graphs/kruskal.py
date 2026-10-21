"""Kruskal's algorithm for the minimum cost spanning tree (exercise 2.2, notes 2.2).

PLACEHOLDER: not implemented yet.
"""

# --- 1. Problem --------------------------------------------------------------
# Same problem as prim.py: minimum cost spanning tree of an undirected,
# connected G = (N, E) with costs c_e.

# --- 2. Inputs and outputs ---------------------------------------------------
# TODO: decide:
#   - Input: here a plain list of edges [(i, j, cost), ...] is the natural choice. Why?
#   - Output: the set F of n - 1 edges and the total cost.

# --- 3. Assumptions and limitations ------------------------------------------
# - Undirected; if not connected you get a spanning FOREST, not a tree: detect it.
# - Any real costs.

# --- 4. Core idea ------------------------------------------------------------
# Start with n isolated nodes (a forest of n components). Scan edges by
# non-decreasing cost and keep an edge only if its endpoints are in different
# components (otherwise it would close a cycle). Prim grows one tree, Kruskal
# grows a forest that merges into one tree.

# --- 5. Pseudocode -----------------------------------------------------------
# TODO: write your pseudocode here.
#
#
#

# --- 6. Python concepts to practice -----------------------------------------
# sorted() with key=, tuple unpacking in for loops, a dict/list as the component
# vector v, (optional) union-find with path compression

# --- 7. Implementation plan --------------------------------------------------
# TODO 1: sort the edges.
# TODO 2: component vector v with v_i = i at start (as in the slides).
# TODO 3: decide how to merge two components (relabel all nodes of one of them).
# TODO 4: stop at n - 1 edges.
# TODO 5: optional: replace the vector with union-find and compare speed.

# --- 8. Complexity -----------------------------------------------------------
# TODO after implementing: cost of sorting? cost of one merge with your relabelling?
# How many merges? Compare with the notes: O(m log n + n^2) for the simple version.

# --- 9. Example to try -------------------------------------------------------
# Same slide graph as prim.py. By hand: sort the edges, mark taken / skipped,
# write v after each merge. Check that the cost equals Prim's.

# --- 10. Tests and edge cases ------------------------------------------------
# - same cost as prim() on several graphs (the trees may differ with ties!)
# - edge that would close a cycle is skipped
# - disconnected graph
# - parallel edges with different costs

# --- 11. Self-check questions ------------------------------------------------
# - Why is a skipped edge never "cost decreasing" for the final tree?
# - When is Kruskal a better choice than Prim's O(n^2) version?
# - What do you change to get a maximum cost spanning tree?


def kruskal(n_nodes: int, edges: list[tuple]) -> tuple[list, float]:
    """Return (F, total_cost) for a minimum cost spanning tree."""
    raise NotImplementedError("TODO")
