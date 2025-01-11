import math
n=int(input())
a=list(map(int,input().split()))

people=[0]*5 #初始化数组，第0-4个数分别代表有0-4个人的小组
for i in a:
    people[i]+=1 #统计每个小组的人数

count=0 #初始化出租车计数器

count+=people[4] #将4人小组的出租车数加到计数器上

if people[3]>=people[1]:
    count+=people[3] #将3人小组和1人小组拼车并带走，剩余的3人小组单独打一辆车
    count+=math.ceil(people[2]/2)#将2人小组拼车，每2组一辆车，向上取整

else:
    count+=people[3] #将3人小组和1人小组拼车并带走
    people[1] -= people[3]  # 计算1人小组剩余的组数

    count+=people[2]//2 #将2人小组拼车，每2组一辆车

    if people[2]%2!=0: #如果2人小组人数为奇数，则最后一辆车和1人小组拼
        count+=1
        people[1]-=2
        if people[1]>0: #如果1人小组还有人
            count+=math.ceil(people[1]/4)

    else: #如果2人小组人数为偶数，则内部消耗完全
        count+=math.ceil(people[1]/4) #每4组一辆车，向上取整

print(count)