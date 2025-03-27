class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        if not nums:
            return 0

        max_prod = nums[0]
        curr_max, curr_min = nums[0], nums[0]

        for i in range(1, len(nums)):
            num = nums[i]
            if num < 0:
                curr_max, curr_min = curr_min, curr_max  # Swap when negative

            curr_max = max(num, curr_max * num)
            curr_min = min(num, curr_min * num)

            max_prod = max(max_prod, curr_max)

        return max_prod




        



        
        