    n = int(input())
    a = list(map(int, input().split()))
     
     
    if n == 0:
        print(0)
        exit()
    j = 1
    count = 1
    for i in  range(1,n):
        if a[i] >= a[i-1]:
            j += 1
        else:
            count = max(j,count)
            j = 1
    count = max(j,count)
    print(count)
