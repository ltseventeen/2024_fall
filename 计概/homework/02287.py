#田忌赛马
while True:
    n = int(input())
    if n == 0:
        break
    tian=list(map(int,input().split()))
    king=list(map(int,input().split()))
    tian.sort()
    king.sort()
    count=0

    ltian=0
    rtian=n-1
    lking=0
    rking=n-1
    while ltian<=rtian and lking<=rking:
        if tian[ltian]>king[lking]:
            count+=1
            ltian+=1
            lking+=1
        elif tian[rtian]>king[rking]:
            count+=1
            rtian-=1
            rking-=1
        else:
            if tian[ltian]<king[rking]:
                count-=1
            ltian+=1
            rking-=1

    print(count*200)