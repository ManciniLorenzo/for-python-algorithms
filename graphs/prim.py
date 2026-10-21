"""Prim's algorithm for the minimum cost spanning tree (slides 2.2 p.4-14).

PLACEHOLDER: not implemented yet.
"""

# --- 1. Problem --------------------------------------------------------------
# Given an undirected, connected G = (N, E) with costs c_e, find a spanning tree
# G_T = (N, T) of minimum total cost. Enumeration is hopeless: K_n has n^(n-2)
# spanning trees (Cayley).

# --- 2. Inputs and outputs ---------------------------------------------------
# TODO: decide:
#   - Input: undirected graph (successor lists or matrix) and a start node u.
#   - Output: the set T of n - 1 edges and its total cost? or the vector closest?

# --- 3. Assumptions and limitations ------------------------------------------
# - Undirected and connected. What happens if the graph is NOT connected? Detect it.
# - Costs can be any real number (negative too): unlike Dijkstra, Prim does not care.
# - Exact regardless of the start node and of how ties are broken (cut property).

# --- 4. Core idea ------------------------------------------------------------
# Grow ONE tree from a start node. S = nodes already in the tree. At each step
# add the cheapest edge of the cut delta(S), i.e. connecting S to N \ S.
# Greedy, and here greedy is exact.

# --- 5. Pseudocode -----------------------------------------------------------
# TODO: write your pseudocode here. Version 1: scan all cut edges each step.
# Version 2 (optional, slides' Algorithm 3): keep C_j and closest_j for j not in S.
#
#
#

# --- 6. Python concepts to practice -----------------------------------------
# sets (S, N \ S), min() with key=, float('inf') / math.inf, tuples for edges,
# frozenset for undirected edges ({1,2} == {2,1}) (optional)

# --- 7. Implementation plan --------------------------------------------------
# TODO 1: simple version: each step, look at all edges with one end in S and one outside.
# TODO 2: stop after n - 1 edges, or report "not connected" if the cut is empty earlier.
# TODO 3: optional: O(n^2) version with C and closest; compare outputs with version 1.
# TODO 4: optional: heapq version for sparse graphs.

# --- 8. Complexity -----------------------------------------------------------
# TODO after implementing: count iterations of each loop in your version.
# Check against the slides: scanning all edges O(nm), with C/closest O(n^2),
# with better data structures O(m log n). Which one did you write?

# --- 9. Example to try -------------------------------------------------------
# Slide example: {1,2}=5, {1,4}=1, {2,3}=3, {2,4}=2, {3,4}=2, {3,5}=5, {4,5}=1.
# Run it by hand from u = 3 writing S and T at each step, then check your code.
# Start again from u = 1: same cost?

# --- 10. Tests and edge cases ------------------------------------------------
# - T has exactly n - 1 edges and touches every node
# - same total cost from every start node
# - ties between edges of equal cost
# - single node graph (T empty)
# - disconnected graph

# --- 11. Self-check questions ------------------------------------------------
# - Which property guarantees that the greedy choice is never wrong?
# - Why are negative costs OK here but not in Dijkstra?
# - How would you get a MAXIMUM cost spanning tree?


def prim(graph: dict, start) -> tuple[list, float]:
    """Return (T, total_cost) for a minimum cost spanning tree."""
    raise NotImplementedError("TODO")
