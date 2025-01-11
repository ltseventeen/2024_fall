n=int(input())
#建立树的列表，其中每棵树的坐标和高度用一个list表示
tree=[list(map(int,input().split())) for _ in range(n)]

count=2 #初始化计数器,有两棵以上的树的时候至少可以砍首尾，并且最右边的树往右砍是特殊情况！

if n==1: #如果只有一棵树，则直接输出
    print(1)

else:
    for i in range(1,n-1):
        if tree[i][0]-tree[i-1][0]>tree[i][1]: #这棵树可以向左砍
            count+=1
        else: #这棵树不能向左砍，考虑向右砍树的情况
            if tree[i+1][0]-tree[i][0]>tree[i][1]: #向右砍树
                count+=1
                tree[i][0]+=tree[i][1] #向右砍树会占用右边的树左边的位置，不妨将这棵树目前的坐标向右移
            else:
                continue
    print(count)