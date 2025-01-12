class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        n = len(nums)
        pref_sum = [0] * n 
        pref_sum[0] = nums[0]

        for i in range(1, n):
            pref_sum[i] = pref_sum[i- 1] + nums[i]



        count = sum( 1 for i in range(n - 1) if pref_sum[i] >= pref_sum[-1] - pref_sum[i])

        return count
        