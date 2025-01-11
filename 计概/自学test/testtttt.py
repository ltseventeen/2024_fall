MAXN = 5
n, m = map(int, input().split())
maze = []
for _ in range(n):
    row = list(map(int, input().split()))
    maze.append(row)

visited = [[False for _ in range(m)] for _ in range(n)]
counter = 0

MAXD = 4
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def is_valid(x, y):
    return 0 <= x < n and 0 <= y < m and maze[x][y] == 0 and not visited[x][y]

def DFS(x, y):
    global counter
    if x == n - 1 and y == m - 1:
        counter += 1
        return
    visited[x][y] = True
    for i in range(MAXD):
        nextX = x + dx[i]
        nextY = y + dy[i]
        if is_valid(nextX, nextY):
            DFS(nextX, nextY)
    visited[x][y] = False

DFS(0, 0)
print(counter)

#相当于是依次试上下左右四个方向能不能走，并且储存visited数组看对应的位置有没有走过，避免回头路无限循环