class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]: 
        mat = [[float('inf')] * numCourses for __ in range(numCourses)]

        for i in range(numCourses):
            mat[i][i] = 0

        
        for i,j in prerequisites:
            mat[i][j] = 1
        
        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    mat[i][j] = min(mat[i][j], mat[i][k] + mat[k][j])
        
        ans = []
        for i,j in queries:
            if mat[i][j] != float('inf'):
                ans.append(True)
            else:
                ans.append(False)

        return ans