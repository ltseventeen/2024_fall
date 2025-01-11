from typing import List
from ast import literal_eval

class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 1
        else:
            dp=[[1]*2 for _ in range(len(nums))]
            for i in range(1,len(nums)):
                if nums[i]>nums[i-1]:
                    dp[i][0]=dp[i-1][1]+1
                    dp[i][1]=dp[i-1][1]
                elif nums[i]<nums[i-1]:
                    dp[i][1]=dp[i-1][0]+1
                    dp[i][0]=dp[i-1][0]
                else:
                    dp[i][0]=dp[i-1][0]
                    dp[i][1]=dp[i-1][1]

            return max(dp[-1])

s=Solution()
print(s.wiggleMaxLength(literal_eval(input())))