class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        '''
        sliding window 

        i    j   
        [1,2,1,4,1]

        subarray == len 3

        '''
        n = len(nums)
        ans = 0
        for i in range(1, n - 1):
            if nums[i] == (nums[i - 1] + nums[i + 1]) * 2:
                ans += 1
        return ans



        # go over the array 
        # i and j pointers within range 3
        # if the sum of i and j == mid and its half
        # return how mmany sum count = return that number


            

            