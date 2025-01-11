t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    move=0
    if a%b==0:
        move=0
    else:
         move=b-a%b
    print(move)
