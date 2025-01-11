from collections import deque

dx=[1,1,1,0,0,-1,-1,-1]
dy=[1,0,-1,1,-1,1,0,-1]

def bfs(x,y,n,m,matrix,area=1):
    q=deque()
    q.append((x,y))
    inq=set()
    inq.add((x,y))
    while q:
        cx,cy=q.popleft()
        for i in range(8):
            nx=cx+dx[i]
            ny=cy+dy[i]
            if 0<=nx<n and 0<=ny<m and matrix[nx][ny]=='W' and (nx,ny) not in inq:
                q.append((nx,ny))
                inq.add((nx,ny))
                area+=1
    return area

t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    matrix=[]
    for _ in range(n):
        matrix.append(list(input()))

    max_area=0
    for i in range(n):
        for j in range(m):
            if matrix[i][j]=='W':
                area=bfs(i,j,n,m,matrix)
                max_area=max(max_area,area)
    print(max_area)