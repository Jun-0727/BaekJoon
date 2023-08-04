import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
M = int(input())

graph = [[] * (N+1) for _ in range(N+1)]
visit = [False] * (N+1)
# visit = [0] * (N+1)

for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def dfs(V):
    visit[V] = True
    for i in graph[V]:
        if not visit[i]:
            dfs(i)

dfs(1)
print(sum(visit) -1)

"""
def bfs(V):
    que = deque([V])
    visit[V] = True
    while que:
        V = que.popleft()
        for i in graph[V]:
            if not visit[i]:
                que.append(i)
                visit[i] = True

# bfs(1)
"""
