class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)

        for u,v,w in times:
            graph[u-1].append((v-1,w))
        
        distances = {node: float('inf') for node in range(n)}
        distances[k-1] = 0
        visited = set()

        pq = [(0,k-1)]


        while pq:
            curr_d , node = heapq.heappop(pq)
            if node in visited: continue

            visited.add(node)
            # print(distances)
            for v,w in graph[node]:
                new_d = curr_d + w
                if new_d < distances[v]:
                    distances[v] = new_d
                    heapq.heappush(pq,(new_d,v))
        if len(visited) == n:
            return max(distances.values())
        return -1