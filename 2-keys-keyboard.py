class Solution:
    def minSteps(self, n: int) -> int:
        cur = 1
        clipboard = 0
        steps = 0
        while cur < n:
            # perform a copy paste operation 
            if n % cur == 0:
                clipboard = cur
                steps += 1
            # perform a paste operation
            cur += clipboard
            steps += 1
        return steps