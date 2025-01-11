from collections import deque
dx=[0,0,1,-1]
dy=[1,-1,0,0]

n=int(input())
maze=[]
for _ in range(n):
    line=list(map(int,input().split()))
    maze.append(line)

def bfs(a1,b1,a2,b2):
    q=deque()
    q.append(((a1,b1),(a2,b2)))
    inq=set()
    inq.add(((a1,b1),(a2,b2)))
    found=False
    while q:
        (x1,y1),(x2,y2)=q.popleft()
        if maze[x1][y1]==9 or maze[x2][y2]==9:
            found=True
            return found

        for i in range(4):
            nx1=x1+dx[i]
            nx2=x2+dx[i]
            ny1=y1+dy[i]
            ny2=y2+dy[i]
            if 0<=nx1<n and 0<=nx2<n and 0<=ny1<n and 0<=ny2<n and maze[nx1][ny1]!=1 and maze[nx2][ny2]!=1 and ((nx1,ny1),(nx2,ny2)) not in inq:
                q.append(((nx1,ny1),(nx2,ny2)))
                inq.add(((nx1,ny1),(nx2,ny2)))

    return found

start=[]
for i in range(n):
    for j in range(n):
        if maze[i][j]==5:
            start.append((i,j))
a1,b1,a2,b2=start[0][0],start[0][1],start[1][0],start[1][1]
result=bfs(a1,b1,a2,b2)
if result:
    print('yes')
else:
    print('no')