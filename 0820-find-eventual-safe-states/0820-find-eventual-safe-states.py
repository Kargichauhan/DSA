class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:



        '''
        Sketch:

        

        Node | Safe
        0       F
        1       F
        2       True
        3       F
        4       T
        5       TRUE
        6       TRUE

        ALGO: 

        hashmap 
        DFS

        TC: 
        
        o(E+V) -> Hashmap (safenode)


        SC:
        '''

        n = len(graph)
        safe = {}

        def dfs(i):
            if i in safe:
                return safe[i]
            safe[i] = False
            for nei in graph[i]:
                if not dfs(nei): return False
            safe[i] = True 
            return safe[i]

        res = []

        for i in range(n):
            if dfs(i): res.append(i)

        return res 
        


