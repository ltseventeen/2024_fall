from collections import deque

dx=[0,0,-1,1]
dy=[1,-1,0,0]

def bfs(x,y,n,m,maze):
    queue=deque()
    queue.append((0,(x,y))) #step,(x,y)
    in_queue={(x,y)}

    while queue:
        step,(x,y)=queue.popleft()
        if x==n and y==m:
            return step

        for i in range(4):
            next_x=x+dx[i]
            next_y=y+dy[i]
            if maze[next_x][next_y]==0 and (next_x,next_y) not in in_queue:
                queue.append(((step+1),(next_x,next_y)))
                in_queue.add((next_x,next_y))

    return -1 #no path found

n,m=map(int,input().split())
maze=[[-1]*(m+2)]+[[-1]+list(map(int,input().split()))+[-1] for i in range(n)]+[[-1]*(m+2)]

print(bfs(1,1,n,m,maze))