class Solution:
    def removeStars(self, s: str) -> str:

        # initial string s
        ans = []

        #iterating over the str to check the pos of *
        for i in s:
            if i == '*':
                ans.pop()

            else: ans += [i]

        return "".join(ans)


        
        
        '''Sketch:

        Str 

        Input: s = "leet**cod*e"
        Output: "lecoe"





        remove * 

        index slicing

        Algo:

        stack

        TC:

        SC:
'''

        


        