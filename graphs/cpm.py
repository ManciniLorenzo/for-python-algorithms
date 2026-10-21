"""Critical Path Method (CPM) for project planning (slides 2.3.5 p.1-16).

PLACEHOLDER: not implemented yet. Builds on dag_shortest_path.py.
"""

# --- 1. Problem --------------------------------------------------------------
# A project = activities with durations d >= 0 and precedences (A_i before A_j).
# Find the minimum overall duration, the earliest/latest time of each event, the
# slack of each activity and a critical path.
# Minimum duration = length of a LONGEST s -> t path in the project DAG.

# --- 2. Inputs and outputs ---------------------------------------------------
# TODO: decide the input level:
#   - Easy start: the activity-on-arc graph is already built (arcs = activities,
#     with dummy arcs of duration 0), nodes numbered topologically.
#   - Harder (optional): a table {activity: (duration, [predecessors])} that you
#     turn into the graph yourself (where do dummies come from?).
# Output: Tmin and Tmax per node, slack per arc, the critical activities.

# --- 3. Assumptions and limitations ------------------------------------------
# - The project graph is a DAG with a single start s and a single end t, and no
#   parallel arcs (that's why dummies exist).
# - Durations are known exactly (no uncertainty: that would be PERT, out of scope).

# --- 4. Core idea ------------------------------------------------------------
# Forward pass in topological order: Tmin of an event = when the LAST entering
# activity can end (max). Backward pass in reverse order: Tmax of an event = the
# latest time that still meets the TIGHTEST following deadline (min).
# Slack of activity (i, j) = Tmax_j - Tmin_i - d_ij; slack 0 = critical.

# --- 5. Pseudocode -----------------------------------------------------------
# TODO: write your pseudocode (forward pass, backward pass, slacks).
#
#
#

# --- 6. Python concepts to practice -----------------------------------------
# reversed(), dicts keyed by tuples (i, j), reusing topological_order from
# dag_shortest_path.py, formatted printing of a table (f-strings with widths)

# --- 7. Implementation plan --------------------------------------------------
# TODO 1: forward pass (can you reuse dag_paths(..., longest=True) directly?).
# TODO 2: backward pass.
# TODO 3: slack for every arc (dummies included).
# TODO 4: list critical activities and one critical path s -> t.
# TODO 5: optional: print a Gantt chart "at earliest" with characters.

# --- 8. Complexity -----------------------------------------------------------
# TODO after implementing: cost of each pass in terms of n and m? Compare with the slides.

# --- 9. Example to try -------------------------------------------------------
# Slide example (2.3.5 p.8-15): activities A..I with durations
# A 3, B 2, C 3, D 3, E 4, F 3, G 1, H 4, I 2 and predecessors
# B:A, C:A, D:C, E:B,C, F:B, G:E,D, H:C, I:F.
# Build the graph by hand (where are the dummies?), do both passes on paper,
# then check the code.

# --- 10. Tests and edge cases ------------------------------------------------
# - Tmin_s = 0 and Tmax_t = Tmin_t
# - every slack >= 0
# - critical activities form an s -> t path
# - an arc with Tmin = Tmax at both ends but slack > 0 (exists in the slide example!)
# - single-activity project

# --- 11. Self-check questions ------------------------------------------------
# - Why max in the forward pass and min in the backward pass?
# - Why is "Tmin = Tmax at both ends" not enough for an activity to be critical?
# - Why must the project graph be acyclic?


def cpm(graph: dict, s, t) -> tuple[dict, dict, dict]:
    """Return (Tmin, Tmax, slack) for an activity-on-arc project graph."""
    raise NotImplementedError("TODO")
