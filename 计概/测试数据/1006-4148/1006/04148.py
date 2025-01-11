n=0

while True:
    p,e,i,d=map(int,input().split())
    if p==e==i==d==-1:
        break

    n+=1
    #先考虑p和e，p的周期是23，e的周期是28
    x=0
    y=0
    while p+23*x<=21252 and e+28*y<=21252:
        if p+23*x<e+28*y:
            x+=1
        elif p+23*x>e+28*y:
            y+=1
        else: #此时p和e的周期重合，考虑i的情况，其周期是33
            if (p+23*x-i)%33!=0:
                x+=28
                y+=23
                continue #此时i的周期不重合，则继续考虑下一个重叠的情况
            elif (p+23*x-i)%33==0: #此时三个周期都重合了！检验其是否大于d
                day=p+23*x
                if day>d:
                    print(f"Case {n}: the next triple peak occurs in {day-d} days.")
                else:
                    print(f"Case {n}: the next triple peak occurs in {day+21252-d} days.")
                break #退出循环