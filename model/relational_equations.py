"""
Created on Dec 28, 2016.

@author: tsabsch
"""


def goedel_implication(x, y):
    """Compute Goedel implication of two values.

    The Goedel implication is defined as 1, if x is smaller than y, and y
    otherwise.

    Args:
        x: An integer value
        y: An integer value

    Returns:
        The goedel implication of x and y.
    """
    if x <= y:
        return 1
    return y


def greatest_solution(fs_X, fs_Y):
    """Find the greatest solution that solves fs_X * solution = fs_Y.

    The greatest solution consists of the goedel implication in each entry.

    Args:
        fs_X: Fuzzy set on X
        fs_Y: Fuzzy set on Y

    Returns:
        Greatest solution of a fuzzy relational equation between fs_X and fs_Y.
    """
    X = fs_X.crisp_set
    Y = fs_Y.crisp_set

    len_X = len(X)
    len_Y = len(Y)

    solution = [[0 for i in range(len_Y)] for i in range(len_X)]
    for i in range(len_X):
        for j in range(len_Y):
            solution[i][j] = goedel_implication(
                fs_X.get_membership_value(X[i]),
                fs_Y.get_membership_value(Y[j]))

    return solution


def greatest_solution_for_all(fss_X, fss_Y):
    """Find the greatest solution that solves all relational equations.

    Finds the greatest solution that solves fss_X[i] * solution = fss_Y[i] for
    i = [1..r]. It is defined as the minimum of the single solutions.

    Args:
        fss_X: FuzzySetOnCrisp
        fss_Y: FuzzySetOnCrisp

    Returns:
        Greatest solution for all relational equations.
    """
    num_eq = len(fss_X)
    eq_solutions = [0] * num_eq

    # compute single goedel solutions
    for i in range(num_eq):
        eq_solutions[i] = greatest_solution(fss_X[i], fss_Y[i])

    # compute global solution
    len_X = len(fss_X[0].crisp_set)
    len_Y = len(fss_Y[0].crisp_set)

    solution = [[0 for i in range(len_Y)] for i in range(len_X)]
    for i in range(len_X):
        for j in range(len_Y):
            solution[i][j] = min(
                [eq_solutions[k][i][j] for k in range(num_eq)])

    return solution
