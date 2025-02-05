class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        '''
        - s1 and s2 are of same length
        - two indices -> one from each string -> swap
        - return true <-possible swap if! = False
        - if same strings -> true

        s1 = "attack" 

        s2 = "defend"

        False

        Algo:

        str -> hashmap -> check each indices in map and if char in the str ->   True

        Indices  i, j = where they will be different

        s1[i] = s2[j] = s1[j], s2[i]

        TC: linear time
        SC: constant space


        '''

        if s1 == s2:
            return True

        indx = [] #collect i, j 
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                indx.append(i)

            if len(indx) > 2:
                return False

        if len(indx) == 2:
            i, j = indx
            return s1[i] == s2[j] and s1[j] == s2[i]


        return len(indx) == 0




        
                

                

    
        