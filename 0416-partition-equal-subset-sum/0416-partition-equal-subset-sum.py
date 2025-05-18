class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums) #sum of array

        if total % 2 != 0:
            return False   #if total sum is odd it cannot be partitioned into = sum subsets

        subset = total//2

        dp = [False] * (subset+1)   #construct a dp table of size(subset+1)
        dp[0] = True

        for curr in nums:       
            for j in range(subset,curr-1,-1):
                dp[j] = dp[j] or dp[j-curr]

        return dp[subset]
