"""Integer Linear Programming: modelling with integer and binary variables.

PLACEHOLDER: Chapter 4 slides are not released yet, so this guide is generic.
Chapter 1 (portfolio selection example) already shows an ILP.
"""

# --- 1. Problem --------------------------------------------------------------
# Some decisions are indivisible (number of trucks) or yes/no (open a facility,
# pick an investment). An ILP is an LP where some variables must be integer
# (x in Z) or binary (x in {0, 1}). Integer LP is NP-hard in general (slides 2.5).

# --- 2. Inputs and outputs ---------------------------------------------------
# - Input: a word problem (from the exercise sets).
# - Output: TODO extend your lp_modelling.py data format with a variable type
#   (continuous / integer / binary).

# --- 3. Assumptions and limitations ------------------------------------------
# - Objective and constraints are still linear.
# - Integrality is NOT a linear constraint: it's a restriction on the variable's domain.
# - Rounding an LP solution is not the same as solving the ILP.

# --- 4. Core idea ------------------------------------------------------------
# For each variable ask: can it take a fractional value in reality? If not,
# integer. Does it represent a yes/no choice? Then binary, and it can switch
# other constraints on/off (e.g. "can produce only if the machine is bought").

# --- 5. Pseudocode -----------------------------------------------------------
# Write your model on paper first: mark next to each variable its domain.
#
#
#

# --- 6. Python concepts to practice -----------------------------------------
# extending an existing data structure, Enum or plain strings for variable types,
# reusing functions from ../linear/lp_modelling.py

# --- 7. Implementation plan --------------------------------------------------
# TODO 1: pick an exercise with indivisible or yes/no decisions.
# TODO 2: list variables with their domain (continuous / integer / binary) and why.
# TODO 3: separate linear constraints from integrality restrictions in your data.
# TODO 4: extend describe_model() to print the domains.

# --- 8. Complexity -----------------------------------------------------------
# TODO: a model with k binary variables has how many 0/1 combinations? Why does
# that make enumeration hopeless (compare with Cayley's n^(n-2) in MST)?

# --- 9. Example to try -------------------------------------------------------
# Portfolio selection style exercise (Chapter 1 or the exercise sets). Write the
# model yourself, then compare with the official solution.

# --- 10. Tests and edge cases ------------------------------------------------
# - feasibility check rejects fractional values for integer variables
# - binary variables accept only 0 and 1
# - a logical constraint (e.g. "at most 2 of these 4") is written linearly

# --- 11. Self-check questions ------------------------------------------------
# - Why is "x is integer" not a linear constraint?
# - Give an example where rounding the LP optimum gives an infeasible or poor solution.
# - How do you write "if y = 0 then x = 0" with a binary y and a bound M?


def describe_ilp(model: dict) -> str:
    """Return the model in algebraic form, with each variable's domain."""
    raise NotImplementedError("TODO")
