class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or k == 0:
            return []
        
        # Max-heap storing tuples: (-value, index)
        max_heap = []
        
        # 1. Initialize the heap with the first k elements
        for i in range(k):
            heapq.heappush(max_heap, (-nums[i], i))
            
        # The top of the heap contains the maximum for the first window
        res = [-max_heap[0][0]]
        
        # 2. Slide the window from index k to the end of nums
        for i in range(k, len(nums)):
            # Add current element to the heap
            heapq.heappush(max_heap, (-nums[i], i))
            
            # LAZY DELETION: Pop elements from top if they fall outside current window [i - k + 1, i]
            while max_heap[0][1] <= i - k:
                heapq.heappop(max_heap)
                
            # The top element is guaranteed to be the maximum valid element in the window
            res.append(-max_heap[0][0])
            
        return res

        

        