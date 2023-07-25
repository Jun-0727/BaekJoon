import sys
from heapq import heappush, heappop

input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
indegree = [0 for _ in range(N+1)]

result = []
heap = []

for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    indegree[B] += 1

for i in range(1, N+1):
    if indegree[i] == 0:
        heappush(heap, i)

while heap:
    tmp = heappop(heap)
    result.append(tmp)

    for i in graph[tmp]:
        indegree[i] -= 1
        if indegree[i] == 0:
            heappush(heap, i)

print(*result)