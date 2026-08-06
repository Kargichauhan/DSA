class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        def scan(lo, hi):                 # inclusive lo, exclusive hi
            prev2 = prev1 = 0
            for i in range(lo, hi):
                prev2, prev1 = prev1, max(prev1, prev2 + nums[i])
            return prev1

        return max(scan(1, n), scan(0, n - 1))
        