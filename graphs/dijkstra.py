"""Dijkstra's algorithm for shortest paths from one origin (slides 2.3 p.3-11).

!!! REQUIRES NON-NEGATIVE ARC COSTS (c_ij >= 0). With a negative arc it can
!!! return a wrong path without any error (slide 2.3 p.11).

PLACEHOLDER: not implemented yet. Your earlier tries are in
dijkstra_attempt_1.py and dijkstra_attempt_2.py: write this one from scratch,
then compare.
"""

# --- 1. Problem --------------------------------------------------------------
# Given a directed G = (N, A) with costs c_ij >= 0 and an origin s, find a
# shortest path from s to EVERY other node.

# --- 2. Inputs and outputs ---------------------------------------------------
# TODO: decide:
#   - Input: successor lists with costs, and s.
#   - Output: labels (L, pred) for every node, as in the slides. L_j = cost of a
#     shortest s -> j path, pred_j = node before j on it.
#   - A separate helper to rebuild the path s -> t from pred.
#   - How do you represent "unreachable"? (L_j = inf, pred_j = None?)

# --- 3. Assumptions and limitations ------------------------------------------
# - c_ij >= 0 for every arc. Decide: check it and raise ValueError, or document it?
# - Negative costs: use floyd_warshall.py, or dag_shortest_path.py if the graph is a DAG
#   (bellman_ford.py is an extra).

# --- 4. Core idea ------------------------------------------------------------
# Make nodes "permanent" in increasing order of distance from s. S = permanent
# nodes (exact labels). At each step the temporary node with the smallest label
# becomes permanent, and its outgoing arcs may improve the labels of the others.
# A permanent label is never changed again: this is exactly what breaks with
# negative arcs.

# --- 5. Pseudocode -----------------------------------------------------------
# TODO: write your pseudocode here without looking at Algorithm 4, then compare.
#
#
#

# --- 6. Python concepts to practice -----------------------------------------
# dict for labels, math.inf, sets, min() with key=, (optional) heapq and the
# "lazy deletion" trick for outdated heap entries

# --- 7. Implementation plan --------------------------------------------------
# TODO 1: initialize L and pred for every node.
# TODO 2: decide how you select the next node: linear scan over temporary nodes, or a priority queue (heapq). Pick ONE first; do the other later if you want.
# TODO 3: update step: which successors do you look at, and when do you change L/pred?
# TODO 4: path reconstruction helper: walk pred back from t.
# TODO 5: decide what happens with unreachable nodes in both functions.

# --- 8. Complexity -----------------------------------------------------------
# TODO after implementing: how many selections, and what does one cost in YOUR version? How many updates overall? The slides give O(n^2) for the array version: does yours match? What changes with a heap?

# --- 9. Example to try -------------------------------------------------------
# Slide 2.3 p.5-10 example (5 nodes, s = 1). Fill the (L, pred) table by hand,
# one row per iteration, then check your code.
# Then the negative-arc example of slide 2.3 p.11 (1->2 cost 2, 1->4 cost 1,
# 2->4 cost -2, 4->3 cost 1): predict the wrong answer before running it.

# --- 10. Tests and edge cases ------------------------------------------------
# - L_s = 0 and pred_s = None
# - unreachable node keeps L = inf
# - two shortest paths of equal cost (any is fine; test the cost, not the path)
# - arc of cost 0
# - negative arc: your chosen behaviour (error or documented wrong result)
# - compare with dijkstra_attempt_1/2 on the same graph (convert the input format)

# --- 11. Self-check questions ------------------------------------------------
# - Why does a negative arc break the "permanent label" argument?
# - Is the union of the shortest paths a minimum spanning tree? Why not?
# - Why can't you just add a constant to every cost to remove negative arcs?


def dijkstra(graph: dict, s) -> tuple[dict, dict]:
    """Return (L, pred): shortest path costs from s and predecessors."""
    raise NotImplementedError("TODO")


def rebuild_path(pred: dict, s, t) -> list:
    """Return the list of nodes of the path s -> t, or [] if t is unreachable."""
    raise NotImplementedError("TODO")
