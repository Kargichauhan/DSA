class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:

        '''
        SKETCH: 

        return i , j , k -> i < j < k
        nums[i] < nums[j] < nums[k]

        if no -> False!

        nums = [1,2,3,4,5]
        Output: true

        nums = [2,1,5,0,4,6]
        Output: true

        nums[3] == 0 < nums[4] == 4 < nums[5] == 6 -> True





        ALGO:


        i to iterate smaller num [i]
        lim - 3 

        n1 []
        n2 []
        n3 []

        pass -> true

        TC: o(n)

        SC: o(n)


        '''

        n1 = float('inf')
        n2 = float('inf')

        for n in nums:
            if n > n2:
                return True
                
            elif (n <= n1):
                n1 = n

            else:
                n2 = n
             
        return False 

            
        

