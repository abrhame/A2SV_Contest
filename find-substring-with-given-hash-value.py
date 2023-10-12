class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        # find the first k letters hash value

        val = 0
        mul = 1

        for i in range(k):
            val += (ord(s[i]) - ord('a') + 1) * mul
            mul = mul * power

        mul = mul // power

        # then find the corresponding hash values by shifting the window. this technique is called rolling hash
        for i in range(len(s) - k + 1):
            if val % modulo == hashValue:
                return s[i:k+i]

            if i < (len(s) - k):
                val = (val - (ord(s[i]) - ord('a') + 1 )) // power + (ord(s[i+k]) - ord('a') + 1 ) * mul