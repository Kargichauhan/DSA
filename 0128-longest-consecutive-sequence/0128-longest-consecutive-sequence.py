class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)

        longest = 0 
        #length = 0 

        for n in nums: #checking the start of sequence 
            if (n-1) not in numSet:
                length = 0 
                while (n + length) in numSet:
                    length += 1 
                longest = max(length, longest)

        return longest
         


        