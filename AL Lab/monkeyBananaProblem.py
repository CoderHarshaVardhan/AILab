def monkey_banana(grid):
    rows = len(grid)
    cols = len(grid[0])
    
    dp = [[0 for _ in range(cols)] for _ in range(rows)]

    for j in range(cols):
        dp[0][j] = grid[0][j]

    for i in range(1, rows):
        for j in range(cols):
            left = dp[i - 1][j - 1] if j > 0 else 0
            right = dp[i - 1][j + 1] if j < cols - 1 else 0
            dp[i][j] = grid[i][j] + max(left, right)

    return max(dp[rows - 1])


grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(monkey_banana(grid))  

