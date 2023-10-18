class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        ans = 0
        dp = [[0,0] for _ in range(len(rating))]

        for i in range(1, len(rating)):
            greaterThans, lessThans = 0, 0 

            for j in range(i):
                if rating[i] > rating[j]:
                    greaterThans += 1
                elif rating[i] < rating[j]:
                    lessThans += 1

            dp[i] = [greaterThans, lessThans]
            # print(dp)
            for j in range(i):
                if rating[i] > rating[j]:
                    ans += dp[j][0]
                elif rating[i] < rating[j]:
                    ans += dp[j][1]


        return ans