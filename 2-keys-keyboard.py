class Solution:
    def minSteps(self, n: int) -> int:
        fact = []
        d = 2
        count = 0
        while d * d <= n:
            while n % d == 0:
                fact.append(d)
                n //= d
            d += 1
        if n > 1:
            fact.append(n)
        # print(fact)

        for i in range(len(fact)):
            count += fact[i]
        return count