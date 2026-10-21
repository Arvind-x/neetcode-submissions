class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        '''
        max k = h
        time for x banana pile = ceil(x/k)
        min k = ? such that sumpiles/k < h
        min k = 1, h
        '''
        import math
        l = 1
        r = max(piles)
        mid = 0
        while l < r:
            mid = (l+r)//2
            time = 0
            for i in range(len(piles)):
                time += math.ceil(piles[i]/mid)
            if time > h:
                l = mid + 1
            else:
                r = mid
        return l