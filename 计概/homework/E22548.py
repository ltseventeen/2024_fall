a=list(map(int,input().split()))
n=len(a)
min_price=float('inf')
max_price=float('-inf')
max_profit=0
for i in range(n):
    if a[i]<min_price:
        min_price=a[i]
        max_price=a[i]
        max_profit=max(max_profit,max_price-min_price)
    if a[i]>max_price:
        max_price=a[i]
        max_profit=max(max_profit,max_price-min_price)
print(max_profit)