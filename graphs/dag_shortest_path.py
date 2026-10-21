"""Shortest and longest paths in a DAG: topological order + dynamic programming
(slides 2.3 p.18-29).

PLACEHOLDER: not implemented yet. cpm.py will reuse both functions.
"""

# --- 1. Problem --------------------------------------------------------------
# Given a directed ACYCLIC graph (DAG) with costs c_ij of ANY sign, find a
# shortest (or longest) path from s to t.
# Longest paths are NP-hard in general graphs, but easy in DAGs.

# --- 2. Inputs and outputs ---------------------------------------------------
# TODO: decide:
#   - topological_order(graph) -> list of nodes, or an error if there is a circuit.
#   - dag_paths(graph, s, longest=False) -> (L, pred) like dijkstra.py.
#   - The DP needs delta-(j) (ENTERING arcs). Your successor lists give delta+.
#     Build predecessor lists, or rewrite the update in "push" form over delta+?

# --- 3. Assumptions and limitations ------------------------------------------
# - The graph must be acyclic: detect a circuit instead of returning garbage.
# - Any costs, negative ones included.

# --- 4. Core idea ------------------------------------------------------------
# Topological order: repeatedly number a node with no entering arcs and delete it.
# In that order every arc goes from a smaller to a larger index, so when you
# reach node j all its predecessors already have their final label:
#     L_j = min over (i, j) in delta-(j) of L_i + c_ij      (max for longest)

# --- 5. Pseudocode -----------------------------------------------------------
# TODO: pseudocode for the topological order AND for the DP pass.
#
#
#

# --- 6. Python concepts to practice -----------------------------------------
# dict of in-degrees, deque, building reverse lists, passing a function or a
# flag to switch min/max (min vs max as values: `choose = max if longest else min`)

# --- 7. Implementation plan --------------------------------------------------
# TODO 1: compute the in-degree of every node.
# TODO 2: topological order with a queue of in-degree-0 nodes; detect leftovers = circuit.
# TODO 3: DP pass in that order; nodes before s in the order: what label do they get?
# TODO 4: longest-path switch.
# TODO 5: reuse rebuild_path from dijkstra.py instead of rewriting it.

# --- 8. Complexity -----------------------------------------------------------
# TODO after implementing: count the work of each phase in terms of n and m.
# Check against the slides' O(n + m).

# --- 9. Example to try -------------------------------------------------------
# Slide 2.3 p.25-27 example (8 nodes, already in topological order, s = 1, t = 8).
# Fill L_1..L_8 and pred by hand, then run the code. Then compute the LONGEST path.
# Also: shuffle the node numbering and check your topological order still works.
# Modelling exercise: machine replacement (slide 2.3 p.29, ex 2.7) as a shortest path.

# --- 10. Tests and edge cases ------------------------------------------------
# - every arc goes forward in your topological order
# - graph with a circuit -> error
# - negative costs
# - shortest and longest give different paths on the same DAG
# - node not reachable from s

# --- 11. Self-check questions ------------------------------------------------
# - Why does the DP fail on a graph with circuits?
# - Why is the longest path easy in a DAG but NP-hard in general?
# - What is the "optimality principle" and where do you use it here?


def topological_order(graph: dict) -> list:
    """Return the nodes in topological order; signal a circuit if there is one."""
    raise NotImplementedError("TODO")


def dag_paths(graph: dict, s, longest: bool = False) -> tuple[dict, dict]:
    """Return (L, pred) from s, shortest by default, longest if longest=True."""
    raise NotImplementedError("TODO")
