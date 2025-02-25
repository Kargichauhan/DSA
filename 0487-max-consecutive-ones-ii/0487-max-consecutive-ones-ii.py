class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxLength = 0
        zeroCount = 0
        start = 0
        for end in range(len(nums)):
            if nums[end] == 0:
                zeroCount += 1
            while zeroCount > 1:
                if nums[start] == 0:
                    zeroCount -= 1
                start += 1

            maxLength = max(maxLength, end - start + 1)
        return maxLength