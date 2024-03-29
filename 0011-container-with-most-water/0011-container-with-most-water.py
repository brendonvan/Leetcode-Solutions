class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = 0;
        
        l = 0
        r = len(height) - 1

        while l < r:
            maxArea = max(maxArea, min(height[l], height[r]) * (r - l))

            if height[l] < height[r]:
                l += 1
            elif height[r] <= height[l]:
                r -= 1
                    
        return maxArea