class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        i = 0
        j = n-1

        def helper(s,i,j,cache):
            if (i, j) in cache:
                return cache[(i, j)]

            # Base Case 1: If there is only 1 character
            if i == j:
                return 1

            # Base Case 2: If there are only 2 characters and both are the same
            if s[i] == s[j] and i + 1 == j:
                return 2

            # If the first and last characters match
            if s[i] == s[j]:
                result = helper(s, i + 1, j - 1, cache) + 2
            else:
                result = max(helper(s, i, j - 1, cache), helper(s, i + 1, j, cache))

            # Cache the result before returning
            cache[(i, j)] = result
            return result
        
        return helper(s,i,j,{})