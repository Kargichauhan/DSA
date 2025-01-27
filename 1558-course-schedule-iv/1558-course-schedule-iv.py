class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        '''
        Sketch: 

        Floyd Warshall Algorithm 

        -> graph 
        -> direct or indirect - course U to course V
        -> matrix

        numCourses = 3

        prerequisites = [[1, 2], [1, 0], [2, 0]]

        queries = [[1, 0], [1, 2]]


        Algo:

        2d matrix:

        reachable [u][v] == True if course U is a prereq of course V 
        else: False

        u -> k and k -> v then u -> v == True

        query (u, v) -> reachable[u] [v]



        TC: 0(n^3)

        SC: 0(n^2)


        '''

        reachable = [[False] * numCourses for _ in range(numCourses)]

        # direct prereq
        for a, b in prerequisites:
            reachable[a][b] = True

        # Floyad - Warshall 
        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    # if i -> k and k -> j, then i -> j 
                    reachable[i][j] = reachable[i][j] or (reachable[i][k] and reachable[k][j])

        answer = []
        for u, v in queries:
            answer.append(reachable[u][v])

        return answer
        