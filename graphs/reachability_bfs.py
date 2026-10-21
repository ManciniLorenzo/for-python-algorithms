"""Graph reachability with a FIFO queue = breadth-first search (slides 2.1 p.8-10, p.16).

PLACEHOLDER: not implemented yet.
"""

# --- 1. Problem --------------------------------------------------------------
# Given a directed G = (N, A) as successor lists and a node s, find the set M
# of all nodes reachable from s. Also reused inside Ford-Fulkerson to find an
# s-t path in the residual network.

# --- 2. Inputs and outputs ---------------------------------------------------
# TODO: decide:
#   - Input: successor lists (from graph_representation.py) and s.
#   - Output: the set M. Also return the order nodes were labelled? A predecessor
#     per node so you can rebuild a path (Ford-Fulkerson will need it)?

# --- 3. Assumptions and limitations ------------------------------------------
# - Works on directed and undirected graphs (undirected = both directions stored).
# - Only finds nodes reachable FROM s: nodes in other parts of the graph are not visited.
# - Costs are ignored.

# --- 4. Core idea ------------------------------------------------------------
# Keep a set Q of nodes reached but not yet processed (the "frontier") and a set
# M of processed (labelled) nodes. Repeatedly take a node from Q, label it, and
# add its successors that are neither in M nor in Q. If Q is managed FIFO the
# exploration goes level by level: breadth-first. Stops when no arc leaves M.

# --- 5. Pseudocode -----------------------------------------------------------
# TODO: write your pseudocode here (compare it with Algorithm 1 in the slides afterwards).
#
#
#

# --- 6. Python concepts to practice -----------------------------------------
# set (membership in O(1) on average), collections.deque (popleft vs list.pop(0):
# why is the second slow?), while loops

# --- 7. Implementation plan --------------------------------------------------
# TODO 1: initialize Q and M.
# TODO 2: main loop: which end of the deque do you take from? which end do you add to?
# TODO 3: decide WHEN you mark a node as "seen" (when added to Q or when popped?)
#         and what goes wrong with the other choice.
# TODO 4: optionally record pred[v] = u when v is added, then rebuild an s -> t path.

# --- 8. Complexity -----------------------------------------------------------
# TODO after implementing: how many times can a node enter Q? How many times is
# each arc looked at? Check your answer against the slides' bound O(n + m).

# --- 9. Example to try -------------------------------------------------------
# Slide example with S(1) = {2,4}, S(2) = {3}, S(3) = {4,5}, S(4) = {2,5}, S(5) = {4}
# and s = 2. Trace Q and M on paper first, then compare with your code's output.
# Then try s = 5: which nodes are reachable?

# --- 10. Tests and edge cases ------------------------------------------------
# - s with no successors: M = {s}
# - graph with a cycle (no infinite loop)
# - node not reachable from s is NOT in M
# - s not in the graph: what should happen?

# --- 11. Self-check questions ------------------------------------------------
# - What changes in the order of exploration if Q is LIFO instead of FIFO? (see dfs.py)
# - Why does the algorithm stop exactly when delta+(M) is empty?
# - In BFS on an unweighted graph, what does the order of labelling tell you about distances from s?


def reachable_nodes(graph: dict, s) -> set:
    """Return the set M of nodes reachable from s."""
    raise NotImplementedError("TODO")
