# army competition

p=int(input())
l = list(map(int, input().split()))

l.sort()

def solution(l, p):
    if p <= l[0]:
        return 0
    
    c = 0
    
    while True:
        for i in range(len(l)):
            if 0<l[i] and l[i]<=p:
                p -= l[i]
                c += 1
                l[i] = 0
        
        ll = [i for i in l if i!=0]
        if not ll:
            break
        
        l = ll

        #print(l,c)
        if c==0 or len(l)==1:
            break
                    
        if l[-1]+p < l[0]:
            break
        
        p += l[-1]
        c -= 1
        l[-1] = 0
    
    return c


print(solution(l,p))