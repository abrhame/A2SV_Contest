from collections import Counter
q = int(input())
for _ in range(q):
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()
    l , r = 0,len(a) - 1
    recatanges = Counter()
    if len(a) % 4 != 0:
        print("NO")
    else:
        while l < r:
            if a[l] != a[l + 1] or a[r] != a[r - 1]:
                break
            s = a[l] * a[r]
            recatanges[s] += 1
            l+=2
            r -= 2
        if n in recatanges.values():
            print("YES")
        else:
            print('NO')
            