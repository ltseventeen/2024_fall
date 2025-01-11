def queue(n,used,one_queue=[]):
    if len(one_queue)==n:
        return [one_queue]

    result=[]
    for i in range(1,n+1):
        if used[i]:
            continue
        else:
            used[i]=True
            result+=queue(n,used,one_queue+[i])
            used[i]=False
    return result

n=int(input())
used=[False]*(n+1)
result=queue(n,used)
for i in result:
    print(' '.join(map(str,i)))