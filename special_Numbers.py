t = int(input())
for i in range(t):
    n,k = map(int, input().split())
    ans = []
    mod = (10**9) + 7 
    k = bin(k)[2:][::-1]
    ans = 0
    for i,val in enumerate(k):
        ans += int(val)*(n**i)
    print(ans%mod)
