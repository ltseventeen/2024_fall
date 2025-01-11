import heapq
pig=[]
heap=[]
def pop1(pig,heap):
    if pig and heap:
        remove=pig.pop()
        if remove==heap[0]:
            heapq.heappop(heap)
        while heap and (heap[0] not in pig):
            heapq.heappop(heap)
    return

def min1(pig,heap):
    if pig and heap:
        result=heap[0]
        return result
    else:
        return -1

def push1(n,pig,heap):
    pig.append(n)
    heapq.heappush(heap,n)
    return

while True:
    try:
        line=list(input().split())
        if line:  #如果输入非空，执行操作
            if line[0]=='pop':
                pop1(pig,heap)
            elif line[0]=='min':
                if min1(pig,heap)==-1:
                    continue
                else:
                    print(min1(pig,heap))
            elif line[0]=='push':
                n=int(line[1])
                push1(n,pig,heap)
        else:  # 遇到空行则停止读取
            break
    except EOFError:  # 当用户输入 EOF (Ctrl+D on Unix, Ctrl+Z on Windows) 时退出循环
        break

