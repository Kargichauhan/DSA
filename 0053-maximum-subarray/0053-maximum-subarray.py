class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sub = max_sub = nums[0]
        for n in nums[1:]:
            curr_sub = max(n, curr_sub + n)
            max_sub = max(max_sub,curr_sub)
        return max_sub

    
        
        
        '''# Initialize our variables using the first element.
        current_subarray = max_subarray = nums[0]

        # Start with the 2nd element since we already used the first one.
        for num in nums[1:]:
            # If current_subarray is negative, throw it away. Otherwise, keep adding to it.
            current_subarray = max(num, current_subarray + num)
            max_subarray = max(max_subarray, current_subarray)

        return max_subarray'''
        