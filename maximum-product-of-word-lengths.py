class Solution:
    def maxProduct(self, words: List[str]) -> int:
        n = len(words)
        map = Counter()

        for word in words:
            mask = 0
            for ch in word:
                pos = ord(ch) - ord("a")
                mask |= 1<<pos
            map[word] = mask
        max_ = 0
        for i in range(n):
            word = map[words[i]]
            for j in range(i+1,n):
                if word & map[words[j]] == 0:
                    max_ = max(max_, len(words[i]) * len(words[j]))
        return max_