class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        c = []
        for c1,c2 in costs:
            c.append((c1 - c2,c1,c2))
        c.sort()
        ans = 0
        for i in range(n):
            if i < n // 2:
                ans += c[i][1]
            else:
                ans += c[i][2]
                

        return ans