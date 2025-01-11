n=int(input())
l=list(map(str,input().split()))
count=0
answer=[]
for i in l:
    count+=len(i)
    if count<=80:
        answer.append(i)
        count+=1
    elif count>80:
        print(' '.join(answer))
        count=len(i)+1
        answer=[i]
print(' '.join(answer))