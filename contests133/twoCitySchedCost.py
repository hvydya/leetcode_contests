details = """
link: https://leetcode.com/contest/weekly-contest-133/problems/two-city-scheduling/
"""
def twoCitySchedCost(self, costs: List[List[int]]) -> int:
    a_c, b_c = 0, 0
    c = 0
    n = len(costs) // 2
    costs.sort(key= lambda x: -abs(x[0] - x[1]))
    for i, j in costs:
        if i < j and a_c != n:
            a_c += 1
            c += i
        elif j < i and b_c != n:
            b_c += 1
            c += j
        elif a_c == n:
            c += j
            b_c += 1
        else:
            c += i
            a_c += 1
    print(c)
    return c
