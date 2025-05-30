class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        
        n = len(nums); pos = [1] * n; neg = [1] * n 



        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    pos[i] = max(pos[i], neg[j] + 1)

                elif nums[j] > nums[i]:
                    neg[i] = max(neg[i], pos[j] + 1)


        return max(max(pos), max(neg))
        