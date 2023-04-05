class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        subsets = []
        ans = [-1,-1]
        def isPrime(num):
            if num < 2:
                return False
            d = 2
            while d * d <= num:
                if num % d ==0:
                    return False
                d+= 1
            return True
        diff = float("inf")
        for num in range(left,right+1):
            if isPrime(num):
                subsets.append(num)
                print(subsets)
                if len(subsets) > 1:
                    tmp = subsets[-1] - subsets[-2]
                    if tmp < diff:
                        diff = tmp
                        ans = [subsets[-2],subsets[-1]]
                        if diff <= 2:
                            break
        return ans