import collections

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        '''
        dominoes[i] = [a,b] == dominoes[j] = [c,d]

        |

        a==c & b==d or (a==d and b==c) -> (i,j)

        dominoes = [[1,2],[2,1],[3,4],[5,6]] -> 1


        '''


        #count the dominos + variable num_pair 

        counts = collections.defaultdict(int)
        num_pairs = 0 


        # loop thru dominoes 

        for domino in dominoes:

            val1 = domino[0]
            val2 = domino[1]


            #cannoical_key = tuple + sorted 
            cannoical_key = tuple(sorted((val1,val2)))
        
            # count -> cannoical key [num_pairs] += counts[cannoical_keys]
            num_pairs += counts[cannoical_key]

            #increment 
            counts[cannoical_key] += 1
        # return num_pairs

        return num_pairs



        



