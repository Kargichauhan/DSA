class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        '''
        Sketch:

        nums = [1, 2, 3, 4]

        Output: [24,12,8,6]

        prefix = [1, 2, 6, 24]

        post fix = [24, 12, 8 , 6]

        output =.     [24,12,8,6]

        

       



        TC: 0(n)

        SC: 0(n) # not take extra memory
        
        '''

        res = [1] * (len(nums))


        prefix = 1 
        for i in range(len(nums)):
            res[i] *= prefix 
            prefix *= nums[i]

        postfix = 1 
        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix 
            postfix *= nums[i]

        return res


        
