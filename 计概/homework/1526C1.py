import heapq
n=int(input())
a=list(map(int,input().split()))
heap=[]
health=0

for i in a:
    heapq.heappush(heap,i)
    health+=i
    if health<0:
        if heap: #确保heap里有元素，防止index error（虽然heap里肯定有元素
            give_up=heapq.heappop(heap)
            health-=give_up #放弃一瓶肯定也就够了，因为它是最负的，而health在喝i之前>=0
print(len(heap))