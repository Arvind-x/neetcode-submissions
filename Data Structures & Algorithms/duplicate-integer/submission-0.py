class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        a = []
        for i in range(0, len(nums)):
            if(nums[i] not in a):
                a.append(nums[i])
            
        
        if(len(a) == len(nums)):
            return False;
        
        return True;
         