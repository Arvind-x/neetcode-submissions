class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict_num = {}
        for num in nums:
            if num in dict_num:
                return True
            else:
                dict_num[num] = 1
        return False


        
         