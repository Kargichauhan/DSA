class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0 
        currS = 0 

        prefixS = {0:1}

        for n in nums:
            currS += n 
            diff = currS - k 

            res += prefixS.get(diff, 0)
            prefixS [currS] = 1 + prefixS.get(currS, 0)


        return res

    