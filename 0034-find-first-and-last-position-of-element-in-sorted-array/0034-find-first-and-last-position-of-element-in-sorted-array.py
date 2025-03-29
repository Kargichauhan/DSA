class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = []
        if target in nums:
            res.append(nums.index(target))
            res.append(len(nums) - nums[::-1].index(target)-1)

            return res
        else: return [-1,-1]



        

        
        