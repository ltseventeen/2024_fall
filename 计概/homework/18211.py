p=int(input())
n=list(map(int,input().split()))
n.sort()
more=0 #初始化最初武器差值

if p<n[0]:
    print(0)

else:
    while more>=0:
        if len(n)==1:
            if p>=n[0]:
                more+=1
                break
            else:
                break
        else:
            if p>=n[0]:
                p-=n[0]
                more+=1
                n=n[1:]
            else:
                p+=n[-1]
                more-=1
                n=n[:-1]

    print(more)