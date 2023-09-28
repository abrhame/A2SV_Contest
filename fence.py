n,k = map(int, input().split())
plank = list(map(int, input().split()))
 
ans = 0
temp = sum(plank[0:k])
com = temp
for i in range(k,n):
    temp -= plank[i-k]
    temp += plank[i]
    if temp < com:
        com = temp
        ans = i-k+1
print(ans+1)
    