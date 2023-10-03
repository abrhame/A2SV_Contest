class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        memo = defaultdict(int)

        def helper(index, currsum):
            if index >= len(stones):
                return abs(currsum)

            if (index, currsum) in memo:
                return memo[(index, currsum)]

            memo[(index,currsum)] = min((helper(index+1, currsum + stones[index])), helper(index + 1, currsum - stones[index]))

            return memo[(index,currsum)]

        return helper(0,0)