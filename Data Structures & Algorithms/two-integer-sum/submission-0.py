class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        find={}
        for i,v in enumerate(nums):
            diff = target-v
            if diff in find:
                return [find[diff],i]
            find[v]=i
        return        