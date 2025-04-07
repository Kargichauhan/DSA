class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        '''

        a,b,c
        f(x) = ax2 + bx + c
        num[i] 


        nums = [-4,-2,2,4]

        a = 1, b = 3, c = 5 

        f(-4) = 1(-4)** 2 + 3(-4) + 5 = -16 + (-12) + 5 = -16 -12 + 5 = -23
        f(-2) = 1(-2) ^ 2 +3(-2) + 5 = -4 + (-6) + 5 = -4  - 6 + 5 = -4 -11 = 9

        '''
        res = []

        for i in range(len(nums)):
            x = nums[i]
            fx = a * x**2 + b * x + c

            res.append(fx)

            res.sort()

        return res






            # 
        