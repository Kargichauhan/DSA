class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        nums = [-1,0,1,2,-1,-4]
        output = [[-1,-1, 2], [-1, 0, 1]]
        '''
        res = []
        nums.sort()

        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i - 1] != nums[i]:
                self.twoSum2(nums, i, res)
        return res 

    def twoSum2(self, nums: List[int], i: int, res: List[List[int]]):
        lo, hi = i + 1, len(nums) - 1
        while lo < hi:
            sum = nums[i] + nums[lo] + nums[hi]
            if sum < 0: 
                lo += 1
            elif sum > 0:
                hi -= 1
            else:
                res.append([nums[i], nums[lo], nums[hi]])
                lo += 1
                hi -= 1
                while lo < hi and nums[lo] == nums[lo - 1]:
                    lo += 1