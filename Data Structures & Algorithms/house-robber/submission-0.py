class Solution:
    def rob(self, nums: List[int]) -> int:
        if nums==[]:
            return 0
        if len(nums)==1:
            return nums[0]
        prev2,prev1=nums[0],max(nums[0],nums[1])
        for i in range(2,len(nums)):
            prev2,prev1=prev1,max(prev1,nums[i]+prev2)
        return prev1
        