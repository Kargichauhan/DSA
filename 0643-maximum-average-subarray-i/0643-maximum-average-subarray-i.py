class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        '''
        arr = nums
        int = k 

        len = k 
        k = avg value 

        return avg value

        -> sliding window


        nums = [1,12,-5,-6,50,3]
        k = 4 

        s1 = [1,12,-5,-6] -> sum = 2
        s2 = [ 12, -5,-6, 50] -> sum = 51 
        s3 = [ -5,-6, 50, 3]. -> sum = 42

        max_sum = 51 

        max_sum/k = 12.75

        o(n) - it is traversing only single time 

        '''

        curr_sum = sum(nums[:k]) # assuming nums as a list of no. and k as an integer

        max_sum = curr_sum

        for i in range(k, len(nums)):
            curr_sum += nums[i] - nums[i - k]
            max_sum = max(max_sum, curr_sum)

        return max_sum/k



        
        