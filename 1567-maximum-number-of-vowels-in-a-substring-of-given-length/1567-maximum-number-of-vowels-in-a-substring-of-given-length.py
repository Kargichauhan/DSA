class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        '''
        vowels = a,e,i,o, u

        s = "abciiidef"
        k = 3 

        sliding window 

        runthru: 

        "abc" = 1                     max_sum = 3
        "bci" = 1
        "cii" = 2
        "iii" = 3
        "..." = ?

        '''

        #step 1 : initalize variables 
        #step 2: count the vowels
        # step3: slide the window through string
        #step 4: return result

        # set of vowels for O(1) lookup to check if a character is a vowel
        vow = set("aeiou")

        # Calculate the number of vowels in the first window of size k
        curr_sum = sum(1 for i in range(k) if s[i] in vow)
        
        max_sum = curr_sum 

        for i in range(k, len(s)): #sliding window
            if s[i] in vow: 
                curr_sum += 1
            if s[i-k] in vow:
                curr_sum -= 1 
            max_sum = max(max_sum, curr_sum)
        #return max 
        return max_sum



        

        