# pylint: skip-file
def sum_ceng(up,down,left,right):
    result=0
    if up==down==left==right:
        result+=onion[up][left]
        return result
    else:
        for i in range(left,right+1):
            result+=onion[up][i]
        for j in range(up+1,down):
            result+=onion[j][left]
            result+=onion[j][right]
        for k in range(left,right+1):
            result+=onion[down][k]
        return result

def dfs(up,down,left,right):
    global max_sum
    if up>down and left>right:
        return
    max_sum=max(max_sum,sum_ceng(up,down,left,right))
    up+=1
    down-=1
    left+=1
    right-=1
    dfs(up,down,left,right)


n=int(input())
onion=[]
for _ in range(n):
    onion.append(list(map(int,input().split())))
up=0
down=n-1
left=0
right=n-1
max_sum=float('-inf')

dfs(up,down,left,right)
print(max_sum)