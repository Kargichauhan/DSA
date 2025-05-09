class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        '''
        two sorted array 
        combine both 
        find median
        '''
        

        merged = sorted(nums1 + nums2)

        n = len(merged)

        if n % 2 == 1:
            return merged[n//2]

        else: return (merged[n//2 - 1] + merged[n//2]) / 2.0


        


     