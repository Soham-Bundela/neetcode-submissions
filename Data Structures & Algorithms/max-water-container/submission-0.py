class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        max_val = min(heights[l],heights[r]) * (r-l)
        
        while l < r:
            if heights[l] >= heights[r]:
                r -= 1
            elif heights[l] < heights[r]:
                l += 1
            curr_val = min(heights[l],heights[r]) * (r-l)
            max_val = max(max_val,curr_val)

        return max_val