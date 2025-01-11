n,m=map(int,input().split())
lst=list(map(int,input().split()))

#把lst中的负数留下，正数和0扔掉，并且降序排序
lst_earn=sorted([abs(x) for x in lst if x<0],reverse=True)
num_earn=len(lst_earn) #计数有多少个电视机可以赚钱

#能搬多少台搬多少
if num_earn<=m:
    print(sum(lst_earn))
else:
    print(sum(lst_earn[:m]))