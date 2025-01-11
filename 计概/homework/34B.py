n,m=map(int,input().split())
l=list(map(int,input().split()))
l.sort()

l_buy=[i for i in l if i<=0]
money=abs(sum(l_buy[:m]))

print(money)