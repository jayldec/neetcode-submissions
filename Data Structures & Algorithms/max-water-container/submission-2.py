class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l=0
        maxw=0
        r=len(heights)-1
        while l<r:
            minimaxwater=(min(heights[l],heights[r]))*(r-l)
            maxw=max(maxw,minimaxwater)
            if heights[l]<heights[r]:
                l=l+1
            else:
                r=r-1
        return maxw

        