"""Graph representation (slides 2.1 p.2-7).

PLACEHOLDER: not implemented yet. Every other file in graphs/ will take a
graph as input, so the choices you make here shape all of them.
"""

# --- 1. Problem --------------------------------------------------------------
# Store a graph G = (N, A) (directed) or G = (N, E) (undirected) so that
# algorithms can ask "which arcs leave node u?" and "what does arc (i, j) cost?".
# The slides give two options:
#   - adjacency matrix n x n: a_ij = 1 (or c_ij) if (i, j) is an arc. For dense graphs
#   - successor lists S(u): for each node, the list of its successors. For sparse graphs
# Start with successor lists (an adjacency list).

# --- 2. Inputs and outputs ---------------------------------------------------
# TODO: decide and write down:
#   - Input: a list of arcs, e.g. [(1, 2), (1, 4), ...] or [(1, 2, 5), ...] with a cost.
#   - Output: your representation. One candidate: dict {node: [(successor, cost), ...]}.
#   - How are nodes named? ints 1..n like the slides, or any hashable label ("A", "B")?
#   - Does every node appear as a key, even with no successors? (Think: node 5 in S(5) = {}.)

# --- 3. Assumptions and limitations ------------------------------------------
# TODO: decide what you allow and what you reject:
#   - directed vs undirected: an undirected edge {i, j} is stored how many times?
#   - parallel arcs (same endpoints twice): allowed? the slides' project graphs forbid them
#   - self-loops (u, u)?
#   - unweighted graphs: what cost do you store, if any?

# --- 4. Core idea ------------------------------------------------------------
# A matrix answers "is (i, j) an arc?" instantly but always costs n^2 memory.
# Successor lists cost memory proportional to n + m and make "iterate over
# delta+(u)" cheap, which is what almost every algorithm in this course does.

# --- 5. Pseudocode -----------------------------------------------------------
# TODO: write your own pseudocode here before coding.
#
#
#

# --- 6. Python concepts to practice -----------------------------------------
# dict, list, tuple, dict.setdefault / collections.defaultdict, list comprehensions
# for the matrix ([[0] * n for _ in range(n)] vs [[0] * n] * n: why is the second wrong?)

# --- 7. Implementation plan --------------------------------------------------
# TODO 1: write build_successor_lists for a directed graph.
# TODO 2: add a `directed` flag; for undirected, store both directions.
# TODO 3: write build_adjacency_matrix (reuse it to compare with the slides' matrix).
# TODO 4: write a tiny helper to print a graph in a readable way (optional).

# --- 8. Complexity -----------------------------------------------------------
# TODO after implementing: memory of each representation in terms of n and m?
# Time to list delta+(u) in each? Time to check if (i, j) is an arc in each?
# Slide reminder: m <= n(n-1) for directed, n(n-1)/2 for undirected.

# --- 9. Example to try -------------------------------------------------------
# Slide 2.1 p.7 directed example: S(1) = {2,4}, S(2) = {3}, S(3) = {4,5},
# S(4) = {2,5}, S(5) = {4}. Build it from a list of arcs and check you get the
# same successor lists. Then draw the 5 x 5 matrix by hand and compare.

# --- 10. Tests and edge cases ------------------------------------------------
# - node with no successors still present
# - undirected edge appears in both lists
# - empty graph (n = 0) and a single node
# - arc mentioning a node outside 1..n (reject? raise ValueError?)

# --- 11. Self-check questions ------------------------------------------------
# - For a graph with n = 1000 and m = 3000, which representation do you pick and why?
# - How do you get delta-(u) (entering arcs) from successor lists? What does it cost?
# - Why does Floyd-Warshall in the slides take a matrix as input while Dijkstra does not need one?


def build_successor_lists(arcs: list[tuple], directed: bool = True) -> dict:
    """Return {node: [(successor, cost), ...]} built from a list of arcs.

    Suggested signature: change it if you choose a different representation.
    """
    raise NotImplementedError("TODO")


def build_adjacency_matrix(n: int, arcs: list[tuple], directed: bool = True) -> list[list]:
    """Return an n x n matrix built from a list of arcs."""
    raise NotImplementedError("TODO")
