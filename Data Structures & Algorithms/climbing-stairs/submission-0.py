class Solution:
    def climbStairs(self, n: int) -> int:
        if n <=1:
            return n
        prev2,prev1=1,1
        for _ in range(2,n+1):
            prev2,prev1=prev1,prev1+prev2
        return prev1

