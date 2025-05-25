class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}

        def bt(index, curr_sum):
            if index == len(nums):
                return 1 if curr_sum == target else 0 


            if (index, curr_sum) in memo:
                return memo[(index, curr_sum)]

            addition = bt(index+1, curr_sum + nums[index])
            subtract = bt(index+1, curr_sum - nums[index])

            memo[(index, curr_sum)] = addition + subtract


            return addition + subtract 


        return bt(0, 0)