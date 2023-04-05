t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = set(a)
    ans = 0
    for i,num in enumerate(a):
        ans = 0
        for j, num1 in enumerate(a):
            if num != num1:
                ans = ans ^ num1
            if ans == num:
                break
        if ans == num:
            break
    print(num)