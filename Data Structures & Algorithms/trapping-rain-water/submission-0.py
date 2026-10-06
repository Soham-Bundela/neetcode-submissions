class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        l_max = height[l]
        r = len(height) - 1
        r_max = height[r]
        
        water = 0

        while l < r:
            if height[l] <= height[r]:
                l += 1
                l_max = max(height[l],l_max)
                water += l_max - height[l]
            elif height[l] > height[r]:
                r -= 1
                r_max = max(height[r],r_max)
                water += r_max - height[r]

        return water