"""Linear Programming: from a word problem to a model.

PLACEHOLDER: Chapter 3 slides are not released yet, so this guide is generic.
Revise it against the slides when they arrive. Chapter 1 (production planning
example) and exercises 1.1-1.4 already show the modelling steps.
"""

# --- 1. Problem --------------------------------------------------------------
# Turn a text description of a decision problem into a linear program:
#     min / max  c^T x   subject to  A x (<=, =, >=) b,  bounds on x
# This file is about MODELLING only. Solving is in lp_solver.py.

# --- 2. Inputs and outputs ---------------------------------------------------
# - Input: a word problem (pick one from the exercise sets, don't invent a new one).
# - Output: TODO decide how to write a model as data in Python, e.g.
#   variable names, objective coefficients, a list of constraints (coefficients,
#   sense, right-hand side), bounds. A plain dict is enough.

# --- 3. Assumptions and limitations ------------------------------------------
# - Linear: objective and constraints are sums of (constant x variable). No x*y, no x^2, no |x|
#   (unless reformulated).
# - Variables are continuous. If some must be integer, see ../integer/ilp_modelling.py.
# - Data (costs, capacities, demands) is assumed known exactly.

# --- 4. Core idea ------------------------------------------------------------
# Ask four questions, in this order:
#   1. What do I decide?             -> decision variables (with units!)
#   2. What do I optimize?           -> objective function (min or max)
#   3. What limits my decisions?     -> constraints
#   4. What values are meaningful?   -> bounds / sign (x >= 0?)

# --- 5. Pseudocode -----------------------------------------------------------
# Not an algorithm here: write the model of your chosen exercise on paper first,
# then translate it into your Python data format.
#
#
#

# --- 6. Python concepts to practice -----------------------------------------
# dicts and lists as structured data, keeping data (parameters) separate from
# the model, printing a model in readable algebraic form with f-strings

# --- 7. Implementation plan --------------------------------------------------
# TODO 1: choose a word problem from materials/exercises.
# TODO 2: write variables, objective, constraints, bounds on paper.
# TODO 3: store the data (parameters) separately from the model structure.
# TODO 4: write a function that prints the model as you would write it on paper.
# TODO 5: optional: a function that checks if a given x is feasible and computes its objective value.

# --- 8. Complexity -----------------------------------------------------------
# TODO: count variables and constraints of your model as a function of the data
# size (e.g. n products, m resources). That's what matters for a solver.

# --- 9. Example to try -------------------------------------------------------
# Take one modelling exercise from ex-1.1-1.2 or ex-1.3-1.4. Check your model
# against the official solution only after writing your own.

# --- 10. Tests and edge cases ------------------------------------------------
# - a point you know is feasible passes your feasibility check
# - a point that violates exactly one constraint fails, and you can tell which one
# - objective value of a hand-computed point matches

# --- 11. Self-check questions ------------------------------------------------
# - What are the units of each variable and of the objective?
# - Is every constraint really linear?
# - Which constraints are "physical" limits and which are logical ones?


def describe_model(model: dict) -> str:
    """Return the model written in readable algebraic form."""
    raise NotImplementedError("TODO")
