"""Ford-Fulkerson algorithm for maximum flow / minimum cut (slides 2.4 p.11-23).

PLACEHOLDER: not implemented yet. Builds on reachability_bfs.py.
"""

# --- 1. Problem --------------------------------------------------------------
# Given a network (directed G, source s, sink t, integer capacities k_ij >= 0),
# find a feasible flow x of maximum value phi. At the end also return a cut
# delta(S*) of minimum capacity: max flow = min cut.

# --- 2. Inputs and outputs ---------------------------------------------------
# TODO: decide:
#   - Input: capacities as a dict {(i, j): k_ij}? successor lists with capacities?
#   - Output: flow x per arc, value phi, and the set S* of the minimum cut.

# --- 3. Assumptions and limitations ------------------------------------------
# - Integer capacities: guarantees termination and an integer optimal flow.
# - The basic version can take a number of iterations proportional to k_max
#   (pseudo-polynomial). Choosing shortest augmenting paths (BFS) = Edmonds-Karp, polynomial.
# - Arcs in both directions between the same pair (i, j) and (j, i): careful with the residual network.

# --- 4. Core idea ------------------------------------------------------------
# Start from x = 0. Build the residual network: a forward residual arc where
# x_ij < k_ij (residual k_ij - x_ij), a backward residual arc where x_ij > 0
# (residual x_ij). An s -> t path in it is an augmenting path: push the
# bottleneck delta along it (+delta forward, -delta backward). When t is no
# longer reachable, the flow is maximum and the reachable nodes form S*.

# --- 5. Pseudocode -----------------------------------------------------------
# TODO: write your pseudocode here.
#
#
#

# --- 6. Python concepts to practice -----------------------------------------
# dicts keyed by tuples, reusing your BFS (needs pred to rebuild the path),
# min() over a generator, keeping two related data structures in sync

# --- 7. Implementation plan --------------------------------------------------
# TODO 1: data structure for the flow x (all zero at start).
# TODO 2: build the residual network from x (a function: easy to test alone).
# TODO 3: find an s -> t path in it with BFS (with pred).
# TODO 4: compute the bottleneck delta and update x: how do you know if a residual
#         arc was forward or backward?
# TODO 5: loop until no path; then S* = nodes reachable from s in the last residual network.

# --- 8. Complexity -----------------------------------------------------------
# TODO after implementing: what does one iteration cost? How many iterations at
# most with integer capacities? Compare with the slides' O(m^2 k_max). Does using
# BFS change the bound (Edmonds-Karp O(n m^2))?

# --- 9. Example to try -------------------------------------------------------
# - Small backward-arc case: capacities all 1, arcs s->1, s->2, 1->2, 1->t, 2->t.
#   Force the first path s->1->2->t and see the backward arc fix it.
# - Slide example 2.4 p.16-18: run it on paper writing x_ij, k_ij on each arc,
#   then compare the final phi and S* with your code.

# --- 10. Tests and edge cases ------------------------------------------------
# - flow balance holds at every intermediate node
# - 0 <= x_ij <= k_ij on every arc
# - phi equals the capacity of the returned cut S*
# - t unreachable from s at start: phi = 0
# - arc of capacity 0

# --- 11. Self-check questions ------------------------------------------------
# - Why is Ford-Fulkerson not greedy?
# - Why do the reachable nodes at the end give a minimum cut?
# - Why can the basic version be exponential in the input size?
# - How would you model a bipartite matching problem as a max flow?


def ford_fulkerson(capacity: dict, s, t) -> tuple[dict, int, set]:
    """Return (x, phi, S_star): maximum flow, its value and a minimum cut."""
    raise NotImplementedError("TODO")
