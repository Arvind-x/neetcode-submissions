class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = 1
        n = len(height)
        if len(height) <= 2:
            return 0
        total = 0
        i = 0
        left = [0] * n
        right = [0] * n
        
        for i in range(1, n):
            left[i] = max(left[i-1], height[i-1])
        for i in range(n-2, -1, -1):
            right[i] = max(right[i+1], height[i+1])
    
        for i in range(0, n):
            if height[i] < min(left[i], right[i]):
                total += min(left[i],right[i]) - height[i]
        return total
            

        