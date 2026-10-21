"""Connected components of an undirected graph.

EXTRA: not a standalone topic in the slides. It shows up inside Kruskal
(ex 2.2: "are the endpoints of e_i in different connected components?").
PLACEHOLDER: not implemented yet.
"""

# --- 1. Problem --------------------------------------------------------------
# Given an UNDIRECTED graph G = (N, E), split N into connected components:
# maximal groups of nodes where every pair is joined by a path.
# (For directed graphs the notion becomes "strongly connected components",
# a different and harder problem: out of scope here.)

# --- 2. Inputs and outputs ---------------------------------------------------
# TODO: decide the output format:
#   - a list of sets [{1, 2, 4}, {3}, ...], or
#   - a component label per node, like the slides' vector v (v_i = component of i),
#     which is exactly what Kruskal needs.

# --- 3. Assumptions and limitations ------------------------------------------
# - Undirected graph, each edge stored in both successor lists.
# - Isolated nodes are components of size 1: they must be in the graph to be found.

# --- 4. Core idea ------------------------------------------------------------
# One traversal (BFS or DFS) from s finds exactly the component of s. Repeat
# from any node not yet assigned until every node has a component.

# --- 5. Pseudocode -----------------------------------------------------------
# TODO: write your pseudocode here.
#
#
#

# --- 6. Python concepts to practice -----------------------------------------
# importing your own function (from graphs.reachability_bfs import reachable_nodes),
# sets and set difference, dict for labels

# --- 7. Implementation plan --------------------------------------------------
# TODO 1: reuse reachable_nodes() (or your DFS) instead of rewriting a traversal.
# TODO 2: loop over all nodes, start a traversal only from unassigned ones.
# TODO 3: produce the output format you chose; maybe offer both.

# --- 8. Complexity -----------------------------------------------------------
# TODO after implementing: each node and edge is processed how many times over ALL
# traversals together? Give the total in terms of n and m.

# --- 9. Example to try -------------------------------------------------------
# Draw an undirected graph with 7 nodes in 3 groups (one of them an isolated node).
# Write the components by hand, then check your output.

# --- 10. Tests and edge cases ------------------------------------------------
# - connected graph: exactly one component
# - graph with no edges: n components
# - isolated node present
# - the union of the components is N and they don't overlap

# --- 11. Self-check questions ------------------------------------------------
# - Why does this approach fail to give "strongly connected components" on a directed graph?
# - In Kruskal, rerunning this whole function after every added edge is wasteful: what's cheaper?
# - How does the number of components change when you add an edge?


def connected_components(graph: dict) -> list[set]:
    """Return the connected components of an undirected graph."""
    raise NotImplementedError("TODO")
