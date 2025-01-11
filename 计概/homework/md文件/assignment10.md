# Assignment #10: dp & bfs

Updated 2 GMT+8 Nov 25, 2024

2024 fall, Complied by <mark>胡杨 元培学院</mark>



**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

2）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

3）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### LuoguP1255 数楼梯

dp, bfs, https://www.luogu.com.cn/problem/P1255

思路：bfs，相当于是看从0通过+1或+2有多少种方法到n，inq用来存已经到达过的数字，当到达n的时候，count+1，返回上一层。

突然想写dp（？），状态转移方程dp[i]=dp[i-1]+dp[i-2]

耗时：10min



代码：

```python
n=int(input())
dp=[0]*(n+1)
dp[0]=1
dp[1]=1
for i in range(2,n+1):
    dp[i]=dp[i-1]+dp[i-2]
print(dp[-1])
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241127203123006](https://s2.loli.net/2024/11/27/caFumoX4gdsPxlI.png)





### 27528: 跳台阶

dp, http://cs101.openjudge.cn/practice/27528/

思路：到达第i阶台阶的方法是到达前面各阶台阶的方法之和，因为从前面的每一台阶都可以直接一步到i（包括第0阶）

耗时：5min



代码：

```python
n=int(input())
dp=[0]*(n+1)
dp[0]=1

for i in range(1,n+1):
    for j in range(i):
        dp[i]+=dp[j]

print(dp[-1])
```



代码运行截图 ==（至少包含有"Accepted"）==

![image-20241127204427152](https://s2.loli.net/2024/11/27/wPnJCIfXWYlpgjK.png)





### 474D. Flowers

dp, https://codeforces.com/problemset/problem/474/D

思路：原本尝试用排列组合的方式实现（如图）然后鼓捣了一个小时发现我的电脑无法承受(10\*\*5)*(10**5)的组合数数据量，CPU差点炸了（x）

<img src="https://s2.loli.net/2024/11/27/Dt8UAduGgKqiTpB.jpg" alt="db5b93e209ae9ce668e40c1465f6e0b"  />

上楼梯的时候突然想通，本题其实是一个一次上一步（吃R花）或者上k步（吃连续k个W花）楼梯的问题，状态转移方程dp[i]=dp[i-1]+dp[i-k]。发现直接对于每一组ab把其间的dp加起来会超时，需要另建一个数组s储存从0到i朵花一共有多少种可以吃

耗时：1h+20min



代码：

```python
t,k=map(int,input().split())
mod=10**9+7
dp=[0]*(10**5+1)
s=[0]*(10**5+1)
dp[0]=1
s[0]=0
for i in range(1,10**5+1):
    if i<k:
        dp[i]=dp[i-1]%mod
    else:
        dp[i]=(dp[i-1]+dp[i-k])%mod
    s[i]=(s[i-1]+dp[i])%mod

for _ in range(t):
    a,b=map(int,input().split())
    answer=(s[b]-s[a-1])%mod
    print(answer)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241128100748108](https://s2.loli.net/2024/11/28/8LN1YwdPgt2mSZC.png)





### LeetCode5.最长回文子串

dp, two pointers, string, https://leetcode.cn/problems/longest-palindromic-substring/

思路：双指针从中间往两边跑，如果序列里从i到j位是回文的，那么从i+1到j-1位也一定是回文的。奇数的情况时，两个指针最初是在同一个位置开始往两边跑；偶数的情况是两个指针本来就在相邻的两个位置，这两个字符相同。

尝试理解马拉车算法并失败，隔段时间再看看

耗时：30min



代码：

```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        if n<2:
            return s
        start,end=0,0
        for i in range(n):
            # odd length palindromes
            l,r=i,i
            while l>=0 and r<n and s[l]==s[r]:
                l-=1
                r+=1
            l+=1
            r-=1
            if r-l+1>end-start+1:
                start,end=l,r
            # even length palindromes
            l,r=i,i+1
            while l>=0 and r<n and s[l]==s[r]:
                l-=1
                r+=1
            l+=1
            r-=1
            if r-l+1>end-start+1:
                start,end=l,r
        return s[start:end+1]
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241202160047242](https://s2.loli.net/2024/12/02/ETi2O6gXmIGPQoZ.png)







### 12029: 水淹七军

bfs, dfs, http://cs101.openjudge.cn/practice/12029/

思路：bfs遍历周围四个点，个人理解要能被淹的条件应该是高度比防水点低？一样高应该淹不了水也被拦住卡那里了？入过队的点就是被淹过了，最后看司令部有没有入过队。

想用bfs的原因是听计概辅导的时候辅导员同学把bfs比喻为从一个迷宫入口倒水，水会经过周围所有的路口并且以最短的时间流到出口。而本题就在倒水（？）

耗时：1h

踩过的坑：

1.数据需要一次性读入，否则会RE

2.split不能加东西，否则会RE，split之后所有空格都被分开，不管什么空格。需要一个index一个一个读入数据

3.需要将比司令部矮的倒水点continue，否则会TLE

4.已经有一个倒水点可以淹掉司令部后，之后的倒水点需要continue，否则会TLE，但不能不读入，否则会RE



代码：

```python
from collections import deque
import sys

dx=[0,0,1,-1]
dy=[1,-1,0,0]

def bfs(x,y):
    q=deque()
    q.append((x,y))
    inq=set()
    inq.add((x,y))
    while q:
        x,y=q.popleft()
        for k in range(4):
            nx=x+dx[k]
            ny=y+dy[k]
            if 0<=nx<m and 0<=ny<n and (nx,ny) not in inq and map_a[nx][ny]<map_a[sx][sy]:
                inq.add((nx,ny))
                q.append((nx,ny))
            if (i,j) in inq:
                return True

    return False

data = sys.stdin.read().split()
k = int(data[0])
index=1
for _ in range(k):
    m,n = map(int, data[index:index+2])
    index+=2
    map_a=[]
    for _ in range(m):
        map_a.append(list(map(int, data[index:index+n])))
        index+=n
    i,j=map(int, data[index:index+2])
    index+=2
    i-=1
    j-=1
    p=int(data[index])
    index+=1
    ans=0
    for _ in range(p):
        sx,sy=map(int, data[index:index+2])
        index+=2
        sx-=1
        sy-=1
        if map_a[sx][sy]<=map_a[i][j]:
            continue
        if ans>0:
            continue
        else:
            if bfs(sx,sy):
                ans+=1

    print("Yes" if ans>0 else "No")
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241202204139883](https://s2.loli.net/2024/12/02/CHdOnWqhMLJm4Dk.png)





### 02802: 小游戏

bfs, http://cs101.openjudge.cn/practice/02802/

思路：相当于是变形的走迷宫，有卡牌的地方是墙，需要加一圈空白的保护圈，因为外面是可以走的，同时也可以使索引和输出对应一些。需要注意x是指纵列，y指的是横行。且最后输出是线段数而不是步数，所以还需要储存每一步走的方向，看它是不是和上一步一样的。步数最少不一定线段数是最少的，保险一点需要储存所有可以到达的走法的线段数，然后输出最小值

踩过的坑：

1.入队条件不能设置为（nx,ny) not in inq，否则可能会漏掉后面一些线段数更少的情况，但是由于其已经进过队了被漏掉

2.如果尝试将入队条件改为（step,nx,ny) not in inq（或者step+1）也不行，会MLE

3.还是得用==dijkstra==，看b站视频学的，首先需要保证权重都是正的，感觉核心思想就是**修改进队条件，并非没有进过队的点可以进队，而是允许一个点重复进队，但是最优/最多/最少的情况才可以重复进队，并且不断更新所需要的那个最优/最多/最少值**

b站讲解：【【算法】最短路径查找—Dijkstra算法】https://www.bilibili.com/video/BV1zz4y1m7Nq?vd_source=c6b3d1a9dcc74a7f8741e4fc1b1ec251

（不是很清楚怎么用语言描述）

耗时：2h



代码：

```python
from collections import deque
direction = [(0,1),(0,-1),(1,0),(-1,0)]

def bfs(step,x,y,pre_dir): #step表示线段数，x，y表示坐标，dir表示上一步前进的方向
    q=deque()
    q.append((0,x,y,-1))
    k=float('inf')
    di=[[float('inf')]*(w+2) for _ in range(h+2)]
    while q:
        step,x,y,pre_dir=q.popleft()
        if x==x2 and y==y2:
            k=di[y][x]
            continue
        for next_dir,(dx,dy) in enumerate(direction):
            nx,ny=x+dx,y+dy
            if next_dir != pre_dir:
                if 0<=nx<w+2 and 0<=ny<h+2 and card[ny][nx]!='X' and di[ny][nx]>step+1:
                    di[ny][nx]=step+1
                    q.append((step+1,nx,ny,next_dir))
            else:
                if 0 <= nx < w + 2 and 0 <= ny < h + 2 and card[ny][nx] != 'X' and di[ny][nx] > step:
                    di[ny][nx] = step
                    q.append((step,nx,ny,next_dir))


    if k!=float('inf'):
        return f'{k} segments.'
    else:
        return 'impossible.'


n=0
while True:
    w,h = map(int,input().split())
    n+=1
    if w == 0 and h == 0:
        break
    print(f'Board #{n}:')
    card=[[' ']*(w+2)]+[[' ']+list(input())+[' '] for _ in range(h)]+[[' ']*(w+2)]
    m=0
    while True:
        x1,y1,x2,y2 = map(int,input().split())
        if x1 == 0 and y1 == 0 and x2 == 0 and y2 == 0:
            break
        m+=1
        card[y2][x2]=' '
        print(f'Pair {m}: {bfs(0,x1,y1,-1)}')
        card[y2][x2]='X'
    print('')
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241203174547988](https://s2.loli.net/2024/12/03/G3xKdHSFXVUwrlt.png)





## 2. 学习总结和收获

<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。</mark>

dfs、bfs都可以遍历所有点，但是**dfs同时会遍历所有路径**，而bfs不一定，**bfs往往可以用于解决最短路径问题**

题目flowers其实是变形的跳楼梯，但是当时并没有顺利地发现这一点，看破复杂问题的包装转化为简单问题的能力有待提高。

目前感觉做起来最痛苦的是递归、dfs和穷举的题目，感觉学了bfs就不想用并忘记了dfs。虽然其他算法也不怎么样。都菜菜的:(

上周没做每日选做，上周大量ddl忙得快死了……日常头痛中……



