t = int(input())
for i in range(t):
        n = int(input())
        arr = list(map(int,input().split()))
        ans=0
        cnt = [0 for i in range(32)]
        for i in range(n):
            msb = -1
            for j in range(30,-1,-1):
                if (arr[i] & (1 << j)):
                    msb = max(msb,j)
            cnt[msb] += 1
        for i in range(len(cnt)):
            if (cnt[i] > 0):
                possible = (cnt[i] * (cnt[i] - 1)) // 2
                ans+=possible
        print(ans)