from collections import deque

p = int(input())
number = input()
lst = list(map(int, number.split()))
lst.sort()
lst = deque(lst)
ans = 0
while lst:
    while lst and p >= lst[0]:
        p -= lst[0]
        lst.popleft()
        ans += 1
    if len(lst) >= 2:
        p += lst[-1]
        lst.pop()
        ans -= 1
print(ans)
