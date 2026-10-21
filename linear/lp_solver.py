"""Linear Programming: using a solver.

PLACEHOLDER: Chapter 3 slides and the labs are not released yet. No solver
library is chosen on purpose: the course labs will say which one (the course
mentions CPLEX or Gurobi). Fill this in when the labs start.
"""

# --- 1. Problem --------------------------------------------------------------
# Given a model already written (lp_modelling.py), get an optimal solution from
# a solver and interpret what comes back.
# Keep the difference clear:
#   - MODELLING = deciding variables, objective, constraints (your job, on paper)
#   - SOLVING   = running an algorithm (e.g. simplex) on that model (the solver's job)

# --- 2. Inputs and outputs ---------------------------------------------------
# - Input: the model data structure from lp_modelling.py.
# - Output: TODO decide: status (optimal / infeasible / unbounded), x*, objective value.

# --- 3. Assumptions and limitations ------------------------------------------
# - The solver is a black box until Chapter 3 explains the simplex method.
# - Floating point: solutions like 2.9999999 are normal; compare with a tolerance.

# --- 4. Core idea ------------------------------------------------------------
# Translate your own model format into the solver's API, call it, then
# translate the answer back into your variable names. Always read the STATUS
# before reading the numbers.

# --- 5. Pseudocode -----------------------------------------------------------
# TODO (when the library is known): write the steps of build -> solve -> read.
#
#
#

# --- 6. Python concepts to practice -----------------------------------------
# installing a package in a virtual environment (.venv is already git-ignored),
# reading library docs, math.isclose for float comparisons

# --- 7. Implementation plan --------------------------------------------------
# TODO 1: wait for the lab to fix the library.
# TODO 2: solve the same model as lp_modelling.py and print the result.
# TODO 3: handle the three outcomes: optimal, infeasible, unbounded.

# --- 8. Complexity -----------------------------------------------------------
# TODO (after Chapter 3): what does the course say about the complexity of LP
# and of the simplex method?

# --- 9. Example to try -------------------------------------------------------
# Your model from lp_modelling.py. Then break it on purpose: remove a constraint
# to make it unbounded, add a contradictory one to make it infeasible.

# --- 10. Tests and edge cases ------------------------------------------------
# - optimal value matches the exercise solution (with a tolerance)
# - infeasible model reports infeasible, not a number
# - unbounded model reports unbounded

# --- 11. Self-check questions ------------------------------------------------
# - What are the four possible outcomes of an optimization problem (Chapter 1)?
# - If the solver says "infeasible", is the model wrong or the data?


def solve(model: dict) -> dict:
    """Return the solver status, the optimal x and the objective value."""
    raise NotImplementedError("TODO")
