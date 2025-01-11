from collections import deque

def bfs(n):
    queue=deque()
    queue.append((0,1))
    in_queue={1}

    while queue:
        step,front=queue.popleft()
        if front==n:
            return step

        if front*2<=n and front*2 not in in_queue:
            queue.append((step+1,front*2))
            in_queue.add(front*2)
        if front+1<=n and front+1 not in in_queue:
            queue.append((step+1,front+1))

n=int(input())
print(bfs(n))
