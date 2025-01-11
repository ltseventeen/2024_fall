n,k=map(int,input().split())
scores=list(map(int,input().split()))
a=scores[k-1]
num=0
if a>0:
    for i in scores:
        if i>=a:
            num+=1
        else:
            continue
else:
    for i in scores:
        if i>0:
            num+=1
        else:
            continue
print(num)