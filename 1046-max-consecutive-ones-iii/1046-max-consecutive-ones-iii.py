class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left, maxL, zeroC = 0, 0, 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zeroC += 1
            while zeroC > k:
                if nums[left] == 0:
                    zeroC -= 1
                left += 1
            maxL = max(maxL, right - left + 1)

        return maxL

                


        