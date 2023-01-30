n = int(input())
arr = list(map(int,input().split()))
l = 0
r = n -1
w = 0
h = 0
while l < r:
    if arr[l]<arr[r]:
        w+=arr[r]
        arr.pop(r)
        r -= 1
    else:
        w+=arr[l]
        arr.pop(l)
        r -= 1
    if arr[l]<arr[r]:
        h+=arr[r]
        arr.pop(r)
        r -= 1
    else:
        h+=arr[l]
        arr.pop(l)
        r -= 1
if n % 2 != 0:
    w+=arr[r]
print(w,h)
