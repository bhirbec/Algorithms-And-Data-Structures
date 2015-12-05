﻿# From Wikipedia (https://en.wikipedia.org/wiki/Edit_distance)
# ============================================================
# In computer science, edit distance is a way of quantifying how dissimilar two strings (e.g., words) are
# to one another by counting the minimum number of operations required to transform one string into the other.
# Edit distances find applications in natural language processing, where automatic spelling correction can
# determine candidate corrections for a misspelled word by selecting words from a dictionary that have a low
# distance to the word in question. In bioinformatics, it can be used to quantify the similarity of macromolecules
# such as DNA, which can be viewed as strings of the letters A, C, G and T.

# From MIT OpenCourseWare (https://youtu.be/ocZMDMZwhCY?t=1441)
# =============================================================
# Given two strings A and B, what's the cheapest possible sequence of character edits to turn A into B?
# Character edits are as follow:
# - insert
# - delete
# - replace

# Recurrence:
# DP(i, j) = min(
#     (cost of inserting Bj) + DP(i, j+1),
#     (cost of deleting Ai) + DP(i+1, j),
#     (cost of replacing Ai -> Bj) + DP(i+1, j+1)
# )

# Base case:
# DP(0,0) = 0

# Time complexity = Theta(|A|.|B|)
# - number of subproblems = Theta(|A|.|B|)
# - time / subproblem = O(1)

def main():
    d = distance('kitten', 'sitting')
    print d

def distance(a, b):
    n, m = len(a), len(b)
    cache = [[None for i in range(m)] for j in range(n)]

    def _distance(i, j):
        if i == n and j == m:
            return 0

        # i has reached n and the cost can only be m - j insertions
        if i == n:
            return m - j

        # j has reached m and the cost can only be n - i deletions
        if j == m:
            return n - i

        cost = cache[i][j]
        if cost is not None:
            return cost

        if a[i] == b[j]:
            cost = _distance(i+1, j+1)
        else:
            cost_replace = _distance(i+1, j+1)
            cost_insert = _distance(i, j+1)
            cost_delete = _distance(i+1, j)
            cost = min(cost_replace, cost_insert, cost_delete) + 1

        cache[i][j] = cost
        return cost

    return _distance(0, 0)

if __name__ == '__main__':
    main()