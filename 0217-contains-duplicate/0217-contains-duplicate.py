class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #hashset - check if the value same then returns true if not than loop out and false 
        #time : 0(n)
        # space : o(n)


        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False

        