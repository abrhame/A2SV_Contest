Copy
n = int(input())
p = list(map(int, input().split()))
ans = "NO"
if n == 2:
    print(ans)
    exit()
for i, val in enumerate(p):
    stack = []
    stack.append(val-1)
    stack.append(p[stack[-1]] - 1)
    stack.append(p[stack[-1]]-1)
    stack.append(p[stack[-1]]-1)
    # stack.append()
    # print(stack)
    # break
    if stack[0] == stack[-1] :
        ans = "YES"
        break
 
print(ans)      
 