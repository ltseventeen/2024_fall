l,m=map(int,input().split())
tree=[1]*(l+1) #有树的地方就标1

for _ in range(m):
    a,b=map(int,input().split())
    for i in range(a,b+1):
        tree[i]=0 #把树枝挖掉

print(sum(tree))