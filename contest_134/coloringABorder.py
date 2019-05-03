def dfs(grid, r0, c0, c):
    if r0 < 0 or c0 < 0 or r0 >= len(grid) or c0 >= len(grid[0]) or grid[r0][c0] != c:
        return
    
    grid[r0][c0] = -c
    dfs(grid, r0 - 1, c0, c), dfs(grid, r0 + 1, c0, c), dfs(grid, r0, c0 + 1, c), dfs(grid, r0, c0 - 1, c)

    if r0 - 1 >= 0 and c0 - 1 >= 0 and r0 + 1 < len(grid) and c0 + 1 < len(grid[0]):
        if abs(grid[r0 - 1][c0]) == c and abs(grid[r0][c0 - 1]) == c and abs(grid[r0 + 1][c0]) == c and abs(grid[r0][c0 + 1]) == c:
            grid[r0][c0] = c
    
def colormat(grid, r0, c0, c):
    dfs(grid, r0, c0, grid[r0][c0])
    
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] < 0:
                grid[i][j] = c
