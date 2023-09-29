from collections import Counter
t = int(input())
 
for ___ in range(t):
    n,m = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    c = Counter(a)
    # print(c)
    for k, v in c.items():
        if (v) >= m:
            ans += m
        else:
            for i in range((v)):
                ans += 1
    
    print(ans)