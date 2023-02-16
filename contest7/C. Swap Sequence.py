#https://codeforces.com/gym/425418/problem/C   
  
  n = int(input())
    a = list(map(int, input().split()))
    count = 0
    ans = []
    for i in range(n):
        tmp = a[i]
        for j in range(i,n):
            if tmp > a[j]:
                tmp = a[j]
                ind = j
        if tmp != a[i]:    
            a[i], a[ind] = a[ind], a[i]
            count += 1
            ans.append([i,ind])
     
    print(count)
    for num in ans:
        print(*num)
        
                    
