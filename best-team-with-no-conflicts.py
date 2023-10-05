class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        n = len(scores)
        arr = [(scores[i], ages[i]) for i in range(n)]
        arr.sort(key=lambda x: (x[1], x[0]))  # Sort players by age and then score

        def calc(idx):
            if idx == n:
                return 0

            if idx in memo:
                return memo[idx]

            m_score = arr[idx][0]  
            for i in range(idx):
                if arr[idx][0] >= arr[i][0]:
                    m_score = max(m_score, arr[idx][0] + calc(i))

            memo[idx] = m_score
            return m_score

        memo = {}
        ans = 0
        for i in range(n):
            ans = max(ans, calc(i))

        return ans