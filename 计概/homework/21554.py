n=int(input())
l=[i for i in range(1,n+1)]
time=list(map(int,input().split()))
time_dict={i:t for i,t in zip(l,time)} #创建编号-时间字典
time_list=sorted(time_dict.items(),key=lambda x:x[1]) #按时间排序

#输出做实验的顺序
shun_xv=[str(item[0]) for item in time_list]
print(' '.join(shun_xv))

#计算平均等待时间
waiting_time=sum(item[1]*(n-1-index) for index,item in enumerate(time_list))
avg_waiting_time=waiting_time/n
print(f'{avg_waiting_time:.2f}')