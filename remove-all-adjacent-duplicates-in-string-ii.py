class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        d = []
        for ch in s:
            if d and ch == d[-1][0]:
                d[-1][1] += 1
                if d[-1][1] == k:
                    d.pop()
            else:
                d.append([ch,1])
        
        ans = ""

        for k,v in d:
            ans += (k * v)
        
        
        return ans