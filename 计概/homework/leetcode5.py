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