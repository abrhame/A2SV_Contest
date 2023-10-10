class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(needle)
        if n == 0:
            return 0
        
        nh = sum((ord(val) * (26 ** (n - 1 - i))) for i, val in enumerate(needle)) % int(1e9)

        m = len(haystack)
        if m < n:
            return -1

        w = 0
        for i in range(n):
            w = (w * 26 + ord(haystack[i])) % int(1e9)

        if w == nh:
            return 0

        for i in range(n, m):
            w = (w * 26 + ord(haystack[i]) - ord(haystack[i - n]) * (26 ** n)) % int(1e9)
            if w == nh:
                return i - n + 1

        return -1