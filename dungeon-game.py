class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        n,m = len(dungeon) - 1, len(dungeon[0]) - 1

        dungeon[n][m] = max(1,1-dungeon[n][m])

        for i in range(n-1,-1,-1):
            dungeon[i][m] = max(1,dungeon[i+1][m]-dungeon[i][m])
        
        for j in range(m-1,-1,-1):
            dungeon[n][j] = max(1,dungeon[n][j+1] - dungeon[n][j])
        
        for i in range(n-1,-1,-1):
            for j in range(m-1,-1,-1):
                dungeon[i][j] = max(1,min(dungeon[i+1][j],dungeon[i][j+1])-dungeon[i][j])

        return dungeon[0][0]