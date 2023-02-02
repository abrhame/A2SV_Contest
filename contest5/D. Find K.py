t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    ans = "NO"
    i = 0
    j = 1
    while j < n:
        diff = a[j] - a[i]
    
        if diff == k:
            ans = "YES"
            break
        # if diff is greater than k, move your left pointer
        elif diff > k:
            i += 1
        # if the diff is less than k, ove your right ponter 
        else:
            j +=1
    print(ans)
