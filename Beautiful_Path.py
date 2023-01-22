from itertools import product
def cross(r, c, ch, grid):
    for i in range(r + 1, len(grid)):
        if grid[i][c] == ".":
            grid[i][c] = ch
        else:
            break

    for i in range(r - 1, -1, -1):
        if grid[i][c] == ".":
            grid[i][c] = ch
        else:
            break

    for j in range(c + 1, m):
        if grid[r][j] == ".":
            grid[r][j] = ch
        else:
            break

    for j in range(c - 1, -1, -1):
        if grid[r][j] == ".":
            grid[r][j] = ch
        else:
            break


inp = map(int, input().split())
n = inp[0]
m = inp[1]

grid = [list(input()) for i in range(n)]

row, col = None, None
row_, col_ = None, None

for i in range(n):
    for j in range(m):
        if grid[i][j] == "S":
            row, col = i, j
        elif grid[i][j] == "T":
            row_, col_ = i, j

        if not row and not col_ :
            break


cross(row, col, "S", grid)
cross(row_, col_, "T", grid)

for i in range(n):
    l = "*"
    for j in range(m):
        if (grid[i][j], l) == ("T", "S") or (grid[i][j], l) == ("S", "T"):
            print("YES")
            exit()

        if grid[i][j] != ".":
            l = grid[i][j]

for j in range(m):
    l = "*"
    for i in range(n):
        if (grid[i][j], l) == ("T", "S") or (grid[i][j], l) == ("S", "T"):
            print("YES")
            exit()

        if grid[i][j] != ".":
            l = grid[i][j]

print("NO")
