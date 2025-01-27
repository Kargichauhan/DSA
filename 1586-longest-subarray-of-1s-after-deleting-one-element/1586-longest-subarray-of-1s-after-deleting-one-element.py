class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left, zeroC, maxL = 0, 0, 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zeroC += 1

            while zeroC > 1:
                if nums[left] == 0:
                    zeroC -= 1
                left += 1

            maxL = max(maxL, right - left)

        return maxL
        