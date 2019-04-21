details = """
link: https://leetcode.com/contest/weekly-contest-133/problems/matrix-cells-in-distance-order/
"""

def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
    a = []
    for i in range(R):
        for j in range(C):
            a.append([i, j])
    return sorted(a, key= lambda x: abs(x[0] - r0) + abs(x[1] - c0))
