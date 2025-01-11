def dfs(a,b,t):
    global result_1,result_2
    if a<=0 or b<=0:
        return
    if t%2==1:
        if a//b>=2 or a==b:
            result_1=True
            return
        else:
            dfs(b,a-b,t+1)
    elif t%2==0:
        if a//b>=2 or a==b:
            result_2=True
            return
        else:
            dfs(b,a-b,t+1)


while True:
    i,j=map(int,input().split())
    x=max(i,j)
    y=min(i,j)
    result_1=False
    result_2=False
    if i==j==0:
        break
    else:
        dfs(x,y,1)
        if result_1:
            print('win')
        elif result_2:
            print('lose')
