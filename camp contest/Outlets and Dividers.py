    t = int(input())
     
    for __ in range(t):
        n,m = map(int,input().split())
        dividers = list(map(int,input().split()))
        dividers.sort()
        total = 0
        if n <= 2:
            print(0)
        else:
            i = len(dividers) - 1
            while i >= 0 and n > 0:
                if total < 1:
                    n -= dividers[i] + 1
                else:
                    n -= dividers[i] - 1
                i -= 1
                total += 1
     
                
            if n <= 0:
                print(total)
            else:
                print(-1)
            
