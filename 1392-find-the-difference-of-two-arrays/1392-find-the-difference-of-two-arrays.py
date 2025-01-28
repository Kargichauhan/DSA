class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        '''
        Sketch:
                        0 1 2.            0 1 2
        Input: nums1 = [1,2,3], nums2 = [2,4,6]

        Output: [[1,3],[4,6]]


        num1[1] = 2 
        num2[0] = 2 

        num1[0] = 1
        num1[2] = 3








        Algo: Set 

        TC: 
3
        SC: 


        '''
        nums1 = set(nums1)
        nums2 = set(nums2)

        ans1 = []
        for num in nums1:
            if num not in nums2:
                ans1.append(num)
            else: nums2.remove(num)

        return [ans1, list(nums2)]



       

        


        