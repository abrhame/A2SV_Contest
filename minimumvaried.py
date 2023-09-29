t = int(input())
 
for ___ in range(t):
    a = input()
    ans = ""
    if len(a) == 1:
        print(int(a))
    else:
        for i in range(9,0,-1):
            temp = sum(int(j) for j in ans)
            if (temp + i) > int(a):
                continue
            ans += str(i)
            if (temp + i) == int(a):
                print(ans[::-1])
                break