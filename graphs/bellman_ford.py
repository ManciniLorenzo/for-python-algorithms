"""Bellman-Ford algorithm for shortest paths with negative costs.

EXTRA: not in the course slides (for negative costs the course uses
Floyd-Warshall, and DP on DAGs). The DP idea behind it is Bellman's (slides 2.3 p.28).
PLACEHOLDER: not implemented yet.
"""

# --- 1. Problem --------------------------------------------------------------
# Given a directed G = (N, A) with costs c_ij of ANY sign and an origin s, find
# shortest paths from s to all nodes, or report that a negative cost circuit
# reachable from s makes the problem ill-defined.

# --- 2. Inputs and outputs ---------------------------------------------------
# TODO: decide:
#   - Input: a list of arcs [(i, j, c_ij), ...] or successor lists, and s.
#   - Output: (L, pred) like dijkstra.py, plus a way to signal a negative circuit
#     (return a flag? raise an exception?).

# --- 3. Assumptions and limitations ------------------------------------------
# - Any costs; a negative circuit NOT reachable from s does not affect the result.
# - Slower than Dijkstra: use it only when negative arcs exist.

# --- 4. Core idea ------------------------------------------------------------
# "Relaxing" an arc (i, j) means: if L_i + c_ij < L_j, improve L_j. A shortest
# path without circuits has at most n - 1 arcs, so relaxing ALL arcs n - 1 times
# is enough. If one more round still improves something, there is a negative circuit.

# --- 5. Pseudocode -----------------------------------------------------------
# TODO: write your pseudocode here.
#
#
#

# --- 6. Python concepts to practice -----------------------------------------
# for loops over a list of tuples, math.inf arithmetic (inf + 5 == inf),
# early exit with break when a round changes nothing, exceptions (raise / custom class)

# --- 7. Implementation plan --------------------------------------------------
# TODO 1: initialize L and pred.
# TODO 2: write the relaxation of one arc. Careful with L_i = inf.
# TODO 3: repeat rounds of relaxation over all arcs; how many rounds at most?
# TODO 4: the extra round for negative circuit detection.
# TODO 5: optional: stop early if a round changes nothing.

# --- 8. Complexity -----------------------------------------------------------
# TODO after implementing: rounds x arcs per round = ? Compare with Dijkstra's O(n^2)
# and Floyd-Warshall's O(n^3) (which solves all pairs).

# --- 9. Example to try -------------------------------------------------------
# - The slide 2.3 p.11 graph where Dijkstra fails: Bellman-Ford should get it right.
# - The slide 2.3 Floyd-Warshall example (it contains the negative circuit 4 -> 2 -> 4):
#   check that you detect it.

# --- 10. Tests and edge cases ------------------------------------------------
# - same result as dijkstra() on graphs with non-negative costs
# - negative arc but no negative circuit
# - negative circuit reachable from s -> detected
# - negative circuit NOT reachable from s -> not reported
# - unreachable nodes stay at inf

# --- 11. Self-check questions ------------------------------------------------
# - Why are n - 1 rounds enough?
# - Why does an improvement in round n prove a negative circuit?
# - When would you pick Floyd-Warshall instead?


def bellman_ford(n_nodes: int, arcs: list[tuple], s) -> tuple[dict, dict]:
    """Return (L, pred) from s; signal a negative circuit reachable from s."""
    raise NotImplementedError("TODO")
