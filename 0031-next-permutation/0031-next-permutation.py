class Solution:
    def nextPermutation(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n <= 1:
            return  # No change needed for lists of size 0 or 1.
        
        # Step 1: Find the first decreasing element from the right
        p = -1
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                p = i
                break
        
        # Step 2: If no such element exists, reverse the entire array
        if p == -1:
            nums.reverse()
            return
        
        # Step 3: Find the smallest element greater than nums[p] to the right of p
        for i in range(n - 1, p, -1):
            if nums[i] > nums[p]:
                # Swap nums[p] and nums[i]
                nums[i], nums[p] = nums[p], nums[i]
                break
        
        # Step 4: Reverse the elements to the right of p
        nums[p + 1:] = reversed(nums[p + 1:])
