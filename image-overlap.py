class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:

        # find all the cells that are 1. find the intersection of theses cells and count the number cells that create the intersectionw
        
        d = defaultdict(int)
        ans = 0
        inter_s1 = []
        inter_s2 = []


        for i in range(len(img1)):
            for j in range(len(img2[0])):
                if img1[i][j] == 1:
                    inter_s1.append([i,j])
                if img2[i][j] == 1:
                    inter_s2.append([i,j])

        for x in inter_s1:
            for y in inter_s2:
                temp = x[0] - y[0],x[1] - y[1]
                d[temp] += 1
                ans = max(ans, d[temp])


        return ans