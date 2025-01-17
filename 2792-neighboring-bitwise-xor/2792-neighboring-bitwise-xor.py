class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        first = 0 
        last = 0 

        for n in derived:
            if n == 1:
                last = ~last #cycle detection 

        return first == last
        