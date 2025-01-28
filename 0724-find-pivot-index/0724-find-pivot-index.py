class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        '''
        Sketch:
        Index of sum of left = sum of ind right 

        ind sum = 0 

        return - 1

        Algo:

        nums = [1,7,3,6,5,6]

        output = 3 

        sum of left = 1 + 7 + 3  = 11
        sum of r = 6 + 5 + 6 11

        return sum 



        TC:

        SC:

        '''

        

        for i in range(len(nums)):

            
            sum_left = sum(nums[0:i])
            sum_right = sum(nums[i+1:])

            if sum_left == sum_right:
                return i

            
        return -1


        

        

        



        