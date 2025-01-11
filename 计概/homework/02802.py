from collections import deque
direction = [(0,1),(0,-1),(1,0),(-1,0)]

def bfs(step,x,y,pre_dir): #step表示线段数，x，y表示坐标，dir表示上一步前进的方向
    q=deque()
    q.append((0,x,y,-1))
    k=float('inf')
    di=[[float('inf')]*(w+2) for _ in range(h+2)]
    while q:
        step,x,y,pre_dir=q.popleft()
        if x==x2 and y==y2:
            k=di[y][x]
            continue
        for next_dir,(dx,dy) in enumerate(direction):
            nx,ny=x+dx,y+dy
            if next_dir != pre_dir:
                if 0<=nx<w+2 and 0<=ny<h+2 and card[ny][nx]!='X' and di[ny][nx]>step+1:
                    di[ny][nx]=step+1
                    q.append((step+1,nx,ny,next_dir))
            else:
                if 0 <= nx < w + 2 and 0 <= ny < h + 2 and card[ny][nx] != 'X' and di[ny][nx] > step:
                    di[ny][nx] = step
                    q.append((step,nx,ny,next_dir))


    if k!=float('inf'):
        return f'{k} segments.'
    else:
        return 'impossible.'


n=0
while True:
    w,h = map(int,input().split())
    n+=1
    if w == 0 and h == 0:
        break
    print(f'Board #{n}:')
    card=[[' ']*(w+2)]+[[' ']+list(input())+[' '] for _ in range(h)]+[[' ']*(w+2)]
    m=0
    while True:
        x1,y1,x2,y2 = map(int,input().split())
        if x1 == 0 and y1 == 0 and x2 == 0 and y2 == 0:
            break
        m+=1
        card[y2][x2]=' '
        print(f'Pair {m}: {bfs(0,x1,y1,-1)}')
        card[y2][x2]='X'
    print('')