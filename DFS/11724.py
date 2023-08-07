import sys
sys.setrecursionlimit(10**6)    # Recursion_Error 해결
def dfs(V):    
    visit[V] = True

    for i in graph[V]:
        if not visit[i]:
            dfs(i)

input = sys.stdin.readline

N,M = map(int, input().split())

graph = [[] * (N+1) for _ in range(N+1)]
visit = [False] * (N+1)

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

count = 0
for i in range(1,N+1):
    if not visit[i]:
        dfs(i)
        count += 1

print(count)