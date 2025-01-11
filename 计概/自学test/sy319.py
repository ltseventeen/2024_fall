from collections import deque

dx=[0,0,1,-1]
dy=[1,-1,0,0]

def dfs(x,y):
    queue=deque()
    queue.append((x,y))
    in_queue.add((x,y))
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            next_x=x+dx[i]
            next_y=y+dy[i]
            if matrix[next_x][next_y]==1 and (next_x,next_y) not in in_queue:
                queue.append((next_x,next_y))
                in_queue.add((next_x,next_y))
    return

n,m=map(int,input().split())
matrix=[[-1]*(m+2)]+[[-1]+list(map(int,input().split()))+[-1] for i in range(n)]+[[-1]*(m+2)]
count=0
in_queue=set()

for i in range(1,n+1):
    for j in range(1,m+1):
        if matrix[i][j]==1 and (i,j) not in in_queue:
            dfs(i,j)
            count+=1

print(count)