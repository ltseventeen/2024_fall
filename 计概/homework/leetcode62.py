class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1] * n for _ in range(m)] #初始化成全部是1的计分矩阵
        #其实主要是把最上面一行和最左边一列初始化为1，因为它们的到达方式均只有1种
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1] #到达(i,j)的路径数等于到达(i-1,j)的路径数+到达(i,j-1)的路径数

        return dp[m-1][n-1] #到达(m-1,n-1)的路径数即为结果

