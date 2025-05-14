class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:    return [-1, -1]

        l, r = 0, len(nums) - 1
        
        while l < r:
            m = (l + r) // 2
            if nums[m] >= target:   r = m
            else:   l = m + 1
        
        if nums[r] != target:   return [-1,-1]

        res = [r]
        l, r =  0, len(nums) - 1

        while l < r:
            m = (l + r + 1) // 2
            if nums[m] <= target:   l = m
            else:   r = m - 1
        
        return res + [l]