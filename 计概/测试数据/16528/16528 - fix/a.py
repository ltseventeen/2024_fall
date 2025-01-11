
def f1(n, l):
    d = [-10000] * 62
    t = dict((i, set()) for i in range(62))
    for i in l: (lambda x:t[x[0]].add(x[1]))(i)
    for i in range(62):
        d[i] = max(d[i], d[i - 1]) if i > 0 else 0
        for k in t[i]: d[k + 1] = max(d[k + 1], d[i] + 1)
    return d[61]

def f2(n, l):
    t = sorted(l, key = lambda x:x[1]-x[0])
    f, ans = [True] * 61, 0
    for x in t:
        if all(f[x[0]:x[1] + 1]):
            ans += 1
            f[x[0]:x[1] + 1] = [False] * (x[1] + 1- x[0])
    return ans

import random



s = 0
for k in range(100):
    n = random.randint(0, 9000)
    l = [sorted([random.randint(0,60), random.randint(0,60)]) for i in range(n)]
    if (f1(n, l) != f2(n, l)):
        s += 1
        with open(str(s) + '.in', mode='w') as file:
            file.write(str(n) + '\n')
            for i in l:
                file.write(str(i[0])+' '+str(i[1])+'\n')
        with open(str(s) + '.out', mode='w') as file:
            file.write(str(f1(n, l)))
        
        

"""

n = int(input())
t = sorted([list(map(int, input().split())) for i in range(n)], key = lambda x:x[1]-x[0])
f, ans = [True] * 61, 0
for x in t:
    if all(f[x[0]:x[1] + 1]):
        ans += 1
        f[x[0]:x[1] + 1] = [False] * (x[1] + 1- x[0])
print(ans)
"""
