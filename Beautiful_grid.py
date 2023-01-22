T = int(input())


def opt(li):
    return min(sum(li), 4 - sum(li))
    
def trim(grid):
    grid = grid[1:-1]
    i = 0
    while i < len(grid):
        grid[i] = grid[i][1:-1]
        i+=1
        
    return grid
    
def func(grid):
    if len(grid) == 1:
        return 0
    elif len(grid) == 2:
        grid[0].extend(grid[1])
        return opt(grid[0])
        
    else:
        minimal = 0
        n = len(grid)
        for i in range(n-1):
            minimal+= opt([grid[0][i], grid[i][n-1], grid[n-1][n-1-i], grid[n-1-i][0]])
        return minimal + func(trim(grid))

for i in range(T):
    n = int(input())
    grid = []
    for i in range(n):
        grid.append(list(map(int ,list(input()))))

    print(func(grid))
