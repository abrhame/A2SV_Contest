class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        map = Counter(deck)
        n = len(deck)
        for i in range(2,n+1):
            if n % i == 0:
                if all(val % i == 0 for val in map.values()):
                    return True
        return False