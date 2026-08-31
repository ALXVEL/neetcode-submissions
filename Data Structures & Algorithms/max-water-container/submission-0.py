class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0
        L, R = 0, len(heights) - 1

        while L < R:   
            if heights[L] < heights[R]:
                maxArea = max(maxArea, (R - L) * heights[L])
                L+=1
            else:
                maxArea = max(maxArea, (R - L) * heights[R])
                R-=1
        
        return maxArea
            