class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        # r = len(nums)
        # while l < r:
        #     mid = (l+r) // 2
        #     # right side is ascending
        #     if nums[mid] < nums[r]:
        #         if target == nums[mid]:
        #             return mid + 1
        #         elif target > nums[mid]:
        #             if target > nums[r]:
        #                 r = mid + 1
        #             else:
        #                 l = mid
        #         else:
        #             r = mid + 1
        #     else:
        #         l = mid
        l = 0
        r = len(nums)-1
        while l < r:
            mid = (l+r) // 2
            if nums[mid] < nums[r]:
                r = mid
            else:
                l = mid +1
                
        if target > nums[-1]:
            #search in 0, l-1
            r = l
            l = 0
        else:
            l = l
            r = len(nums)-1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return -1





        