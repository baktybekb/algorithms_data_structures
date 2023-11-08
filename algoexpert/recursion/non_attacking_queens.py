# https://www.algoexpert.io/questions/non-attacking-queens

# O(~n!) time, less than n!
# O(n) space, recursive call stack
def nonAttackingQueens(n):
    placements = [0]
    cols = set()
    up_diagonal = set()
    down_diagonal = set()

    def helper(row):
        if row == n:
            placements[0] += 1
            return
        for col in range(n):
            if col in cols or row + col in up_diagonal or row - col in down_diagonal:
                continue
            cols.add(col)
            up_diagonal.add(row + col)
            down_diagonal.add(row - col)
            helper(row + 1)
            cols.remove(col)
            up_diagonal.remove(row + col)
            down_diagonal.remove(row - col)

    helper(0)
    return placements[0]
