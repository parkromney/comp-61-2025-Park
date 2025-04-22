grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

def sum_region(grid, row=0, col=0):
    if row >= len(grid):
        return 0
    if col >= len(grid[row]):
        return sum_region(grid, row + 1,0)
    return grid[row][col] + sum_region(grid, row, col + 1)

result=sum_region(grid)
print(result)

