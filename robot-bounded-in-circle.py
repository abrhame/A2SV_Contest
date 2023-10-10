class Solution:
    def isRobotBounded(self, instructions: str) -> bool:

        dir='n'
        turn_left = {'n':'w', 'w':'s', 's':'e', 'e':'n'}
        turn_right = {'n':'e', 'w':'n', 's':'w', 'e':'s'}
        x = 0
        y = 0
        for i in instructions:
            if i=='L':
                dir = turn_left[dir]
            elif i=='R':
                dir = turn_right[dir]
            else:
                if dir=='n':
                    y+=1
                if dir=='s':
                    y-=1                
                if dir=='w':
                    x-=1
                if dir=='e':
                    x+=1
        if dir=='n' and (x!=0 or y!=0):
            return False
        return True