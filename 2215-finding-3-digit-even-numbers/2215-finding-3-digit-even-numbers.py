class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        
        '''
        breakdown:
        -> three digits with even numbers
        -> form 3 digits 
        
        Approach:
        -> counting the freq of each digit from the input list 
        -> loop thru all 3 digit even no. from 100 to 998
        -> for each no. spilt into its digits 
        -> check if it can be built using given digits (comparing frequencies)
        -> if yes --> add to result list 

        and return list of all such numbers

        complexity:
        -> o(900.d) = o(900)
        -> o(1) = fixed size frequency maps
        '''

        from collections import Counter
        freq = Counter(digits)
        res = []

        for num in range(100,1000,2):
            parts = [num // 100, (num // 10) % 10, num % 10]
            count = Counter(parts)
            if all (freq[d] >= count[d] for d in count):
                res.append(num)

        return res

