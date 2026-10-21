"""Floyd-Warshall algorithm: shortest paths between all pairs (slides 2.3 p.12-17).

PLACEHOLDER: not implemented yet.
"""

# --- 1. Problem --------------------------------------------------------------
# Given a directed G = (N, A) with costs c_ij of any sign, find a shortest path
# between EVERY pair of nodes, or detect a circuit of negative cost (problem
# not well-defined).

# --- 2. Inputs and outputs ---------------------------------------------------
# - Input: n x n cost matrix C (as in the slides). TODO: how do you mark "no arc"?
# - Output: matrices D (d_ij = shortest cost i -> j) and P (p_ij = predecessor
#   of j on that path), plus a negative-circuit signal.
# TODO: nodes are 1..n on paper but Python lists start at 0. Decide how to map them.

# --- 3. Assumptions and limitations ------------------------------------------
# - Any costs. With a negative circuit the result is meaningless: you must stop and report.
# - O(n^2) memory: fine for small n.

# --- 4. Core idea ------------------------------------------------------------
# Triangular operation: for a node u, is it cheaper to go i -> u -> j than the
# best i -> j found so far? Apply it for every u in turn. After processing u,
# d_ij is the best cost using only intermediate nodes in {1, ..., u}.
# A negative value on the diagonal (d_ii < 0) means a negative circuit through i.

# --- 5. Pseudocode -----------------------------------------------------------
# TODO: write your pseudocode here, including the initialization of D and P.
#
#
#

# --- 6. Python concepts to practice -----------------------------------------
# nested lists, building a matrix correctly ([[...] for _ in range(n)]),
# copy vs reference (copy.deepcopy), triple nested loops, range()

# --- 7. Implementation plan --------------------------------------------------
# TODO 1: initialize D (0 on the diagonal, c_ij if arc, inf otherwise) and P (p_ij = i).
# TODO 2: the triangular operation, inside three loops. Which loop is the outermost? Why does it matter?
# TODO 3: negative circuit check on the diagonal.
# TODO 4: helper to rebuild the path i -> j from P.
# TODO 5: don't modify the caller's matrix C.

# --- 8. Complexity -----------------------------------------------------------
# TODO after implementing: count the triangular operations. Compare with the slides' O(n^3).
# Compare with running dijkstra() once per node: when is that better?

# --- 9. Example to try -------------------------------------------------------
# Slide example: arcs (1,2)=2, (1,4)=1, (2,3)=3, (2,4)=3, (3,2)=2, (4,2)=-5, (4,3)=5.
# By hand, write D0 and P0, then process u = 1 and u = 2 crossing out row/column u.
# Predict where the algorithm stops and why, then run the code.
# Then change (4,2) to cost -1 and solve the whole thing.

# --- 10. Tests and edge cases ------------------------------------------------
# - graph without negative arcs: D matches dijkstra() run from every node
# - negative arcs, no negative circuit
# - negative circuit detected
# - unreachable pair stays inf
# - input matrix unchanged after the call

# --- 11. Self-check questions ------------------------------------------------
# - What does d_ij mean after processing the first u nodes?
# - Why does a negative d_ii reveal a negative circuit?
# - Why does p_ij become p_uj (and not u) when the triangular operation improves d_ij?


def floyd_warshall(cost_matrix: list[list]) -> tuple[list[list], list[list]]:
    """Return (D, P); signal a negative cost circuit if one exists."""
    raise NotImplementedError("TODO")
