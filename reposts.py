from collections import defaultdict,deque
 
n = int(input())
graph = defaultdict(list)
 
for _ in range(n):
    string = list(input().split())
    string = [s.lower() for s in string]
    graph[string[2]].append(string[0])
 
queue = deque()
visited = set()
for elem in graph['polycarp']:
    queue.append(elem)
    visited.add(elem)
count = 1
while queue:
    n = len(queue)
    count += 1
    for _ in range(n):
        node = queue.popleft()
        for elem in graph[node]:
            queue.append(elem)
print(count)   