t=int(input())

for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))

    a_min=min(a)
    b_min=min(b)
    answer1=a_min*n+sum(b) #位于最小行的方案
    answer2=b_min*n+sum(a) #位于最小列的方案
    print(min(answer1,answer2))