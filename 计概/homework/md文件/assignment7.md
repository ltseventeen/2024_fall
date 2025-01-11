# Assignment #7: Nov Mock Exam立冬

Updated 1646 GMT+8 Nov 7, 2024

2024 fall, Complied by <mark>胡杨 元培学院</mark>



**说明：**

1）⽉考： <mark>AC3</mark> 。考试题⽬都在“题库（包括计概、数算题目）”⾥⾯，按照数字题号能找到，可以重新提交。作业中提交⾃⼰最满意版本的代码和截图。

2）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

3）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

4）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### E07618: 病人排队

sorttings, http://cs101.openjudge.cn/practice/07618/

思路：首先根据年龄大小分类，60岁及以上的放在前面按年龄排，60岁以下的在后面按顺序排

考试时耗时：30min

体现了笨人一个巨大的问题就是 ==没有思维难度的但是有写代码难度的题思路清晰但是不知道怎么写==

而且==考场上大脑空空的写了好久，自己下来写几分钟就搞定了==



题解启示：**`elderly.sort(key=lambda x: -x[1])`把年龄改成负数也可以实现从大到小排序！**

不过我个人改reverse=True好像改习惯了，但这种控制lambda函数的方法或许可以用于某些不能直接reverse=True的情况



代码：

```python
n=int(input())
old=[]
normal=[]

for _ in range(n):
    name,age=input().split()
    age=int(age)
    if age>=60:
        old.append((name,age))
    else:
        normal.append((name,age))

sort_old=sorted(old,key=lambda x:x[1],reverse=True)
l=sort_old+normal
name_list=[name for name,age in l]

print('\n'.join(name_list))

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241112103715137](https://s2.loli.net/2024/11/12/g467wLPqAJWjSer.png)





### E23555: 节省存储的矩阵乘法

implementation, matrices, http://cs101.openjudge.cn/practice/23555/

思路：先把XY都初始化成全是0的矩阵，然后根据三元组的表示方法把其中不是0的数填进去，然后根据矩阵乘法的规则相乘，然后把不是0的地方按三元组输出

主要问题是矩阵乘法不会啊！！老师答应我下次不要考高数线代普化普物知识好嘛o(TヘTo)

考试时耗时：30min



题解启示：

```python
c = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        c[i][j] = sum(a[i][k] * b[k][j] for k in range(n))
        if c[i][j] != 0:
            print(i, j, c[i][j])
```

**发现不是0的值可以直接输出！节省一套遍历c矩阵的循环**

非常简单的想法，但是自己就是想不到



代码：

```python
n,m1,m2=map(int,input().split())
a=[[0]*n for _ in range(n)]
b=[[0]*n for _ in range(n)]

#修改矩阵a,b的值
for _ in range(m1):
    i,j,num=map(int,input().split()) #第i行，第j列，值为num
    a[i][j]=num #i，j均从0开始

for _ in range(m2):
    i,j,num=map(int,input().split())
    b[i][j]=num

#计算乘法
c=[[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        #C[i][j] = A[i][0]*B[0][j] + A[i][1]*B[1][j] + …… +A[i][n-1]*B[n-1][j]
        c[i][j]=sum(a[i][k]*b[k][j] for k in range(n))

#将c整理为三元组形式
result=[]
for i in range(n):
    for j in range(n):
        if c[i][j]!=0:
            result.append(f'{i} {j} {c[i][j]}')

#输出结果
print('\n'.join(result))
```



代码运行截图 ==（至少包含有"Accepted"）==

![image-20241112105424779](https://s2.loli.net/2024/11/12/1jYlXMP3Ln4rmDi.png)





### M18182: 打怪兽 

implementation/sortings/data structures, http://cs101.openjudge.cn/practice/18182/

思路：

考试时耗时：30min，然后模拟写不出来了心态炸了，跳过

题解启示：先在群里看到了defaultdict和heapq两个用法，学习一下





代码：

```python

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>





### M28780: 零钱兑换3

dp, http://cs101.openjudge.cn/practice/28780/

思路：相当于完全背包问题，如果没有填满背包（没有完全兑换零钱），可以把值设定为+inf，这样子就不会影响dp的过程了！（反正取最小，+inf怎么样都不会取到它的）

时限很长，于是就放心的写了

考试时耗时：大约15min



代码：

```python
n,m=map(int,input().split())
worth=list(map(int,input().split()))
dp=[0]+[float('+inf')]*m

for i in range(1,m+1):
    for j in range(n):
        if i>=worth[j]:
            dp[i]=min(dp[i],dp[i-worth[j]]+1)

if dp[-1]==float('+inf'):
    print('-1')
else:
    print(dp[-1])
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241112112521308](https://s2.loli.net/2024/11/12/oLCdFGeHW34wDm7.png)





### T12757: 阿尔法星人翻译官

implementation, http://cs101.openjudge.cn/practice/12757

思路：由于可能出现hundred在million或者thousand前面的情况，所以不能直接换算成数字然后求和。可以遇到million时结算一次，继续翻译，遇到thousand时再结算一次

耗时：考试的时候没看，自己做20min



代码：

```python
num_dict={'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, "nine":9, "ten":10, 'eleven':11, 'twelve':12, 'thirteen':13, 'fourteen':14, 'fifteen':15, 'sixteen':16, 'seventeen':17, 'eighteen':18, 'nineteen':19, 'twenty':20, 'thirty':30, 'forty':40, 'fifty':50, 'sixty':60, 'seventy':70, 'eighty':80, 'ninety':90, 'hundred':100, 'thousand':1000, 'million':1000000}
word=list(map(str,input().split()))
result=0
temp=0
a=1

if word[0]=='negative':
    a=-1
    word=word[1:]

for i in word:
    if i in ('thousand','million'):
        result+=temp*num_dict[i]
        temp=0
        continue

    if i=='hundred':
        temp*=100
        continue

    else:
        temp+=num_dict[i]

result+=temp
print(result*a)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241112215543793](C:\Users\胡杨\AppData\Roaming\Typora\typora-user-images\image-20241112215543793.png)





### T16528: 充实的寒假生活

greedy/dp, cs10117 Final Exam, http://cs101.openjudge.cn/practice/16528/

思路：将所有活动按照结束的时间排序，结束时间相同的活动选择开始时间最晚的一项的一项（因为同时结束的活动必然只能参加一个，而参加开始时间最晚的活动将给其他活动留出时间）。如果当天没有活动结束，则当天累积的参加活动次数应该等于前面天数中参加活动数量的最大值。如果当天有活动结束，则考虑继承当天前一天数值和开始前一天的活动数+1，取最大



代码：

```python
n=int(input())
act=[[-1] for _ in range(62)]
for _ in range(n):
    s,e=map(int,input().split())
    act[e+1].append(s+1)

dp=[0]*62
for i in range(1,62):
    if max(act[i])==-1:
        for j in range(i):
            dp[i]=max(dp[i],dp[j])
    else:
        a=max(act[i])
        dp[i]=max(dp[i-1],dp[a-1]+1)

print(max(dp))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241112220023471](C:\Users\胡杨\AppData\Roaming\Typora\typora-user-images\image-20241112220023471.png)





## 2. 学习总结和收获

<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。</mark>

（现在是北京时间22:10分，苯人已经从早八连续干到了现在，实在干不动了打怪兽明天再打吧X(

本次月考发现的问题：

1.思维难度较低的题目耗时过久，比如两道easy题目，和计概很好的同学探讨了一下觉得应该是我对各种基础语法不熟练。鉴定为题做少了，以后1000以下的每日选做一天3道+，1000以上一天2道X(，不做完不准吸猫（x）

完全知道应该怎么做但就是不会写的感觉太折磨了

2.草稿纸是个好东西，带草稿纸是很必要的！

3.后面的题不一定就比前面的难，每道题至少都要看一看，比如说本次的翻译官一题对于我还算比较好写，但是最后的时间都在死磕寒假生活。浪费太久时间还是写不出来的话及时放弃

半期之前的时间全部献给了高数，终于考完了，到现在依然处于透支学习的精神恍惚阶段X(每天和头痛斗争中X(

总之能活着的话加油吧



