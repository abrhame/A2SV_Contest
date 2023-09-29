N,D = map(int, input().split())
player = list(map(int, input().split()))
player.sort(reverse=True)
 
right = N - 1
num_of_wins = 0
for left in range(N):
    if left > right: break
    
    power = player[left]
    while right > left and power <= D:
        power += player[left]
        right -= 1
    
    num_of_wins += int(power > D)
    
print(num_of_wins)
    