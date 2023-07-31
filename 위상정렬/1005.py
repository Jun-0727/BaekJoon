import sys
from collections import deque

input = sys.stdin.readline
result = []
T = int(input())

for _ in range(T):
    N, K = map(int, input().split())    # 건물의 개수 N, 건설순서 규칙 개수 K
    graph = [[] for _ in range(N+1)]    # 1~N번 까지의 건물의 그래프 리스트
    indegree = [0 for _ in range(N+1)]  # 1~N번 건물의 진입차수 리스트
    DP = [0 for _ in range(N+1)]        # 해당 건물까지 걸리는 시간 리스트
    time = [0] + list(map(int, input().split()))  # 건물당 건설에 걸리는 시간 리스트
    que = deque()

    # 건물간 건설 순서 설정
    for _ in range(K):
        X, Y = map(int, input().split())
        graph[X].append(Y)
        indegree[Y] += 1

    W = int(input())    # 승리를 위해 건설해야 할 건물의 번호

    # 1~N번 까지의 건물 중, 진입차수가 0인 건물을 heap 리스트에 push    
    for i in range(1, N+1):
        if indegree[i] == 0:
            que.append(i)
            DP[i] = time[i]     # 해당 건물까지 짓는데 걸리는 시간 초기화
    
    # 큐에 들어있는 건물을 하나씩 꺼내서 건물짓는데 걸리는 시간 확인
    while que:
        temp = que.popleft()
        for i in graph[temp]:
            indegree[i] -= 1
            DP[i] = max(DP[temp] + time[i], DP[i])   # 해당 건물까지 짓는데 걸리는 시간 초기화
            if indegree[i] == 0:
                que.append(i)
    
    result.append(DP[W])

for x in result:
    print(x)