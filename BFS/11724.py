import sys
from collections import deque

input = sys.stdin.readline
N,M = map(int, input().split())

graph = [[]*(N+1) for _ in range(N+1)]
visit = [False] * (N+1)

for _ in range(M):
    u, v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

def bfs(V):
    que = deque([V])
    visit[V] = True

    while que:
        V = que.popleft()
        
        for i in graph[V]:
            if not visit[i]:
                que.append(i)
                visit[i] = True

count = 0
for i in range(1, N+1):
    if not visit[i]:
        bfs(i)
        count += 1
print(count)