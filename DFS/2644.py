import sys
sys.setrecursionlimit(10**6)
iuput = sys.stdin.readline

n = int(input())                    # 전체 사람의 수 입력
p1, p2 = map(int, input().split())  # 촌수를 계산해야 하는 서로 다른 두 사람의 번호 입력
m = int(input())                    # 부모 자식들 간의 관계의 개수 입력

graph = [[] * (n+1) for _ in range(n+1)]    # 그래프 생성
check = [False] * (n+1)                     # 방명록 생성
find = False                                # 친척 관계 찾은 여부

# m개 만큼 부모 자식간의 관계를 나타대는 두 번호 입력
for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)


# dfs 함수 정의
def dfs(p1,p2,count):
    global find
    count += 1
    check[p1] = True

    for p in graph[p1]:     # p1과 관계를 갖고 있는 사람 중
        # 찾은 경우
        if p2 == p:         
                find = True
                print(count)
                return
        if not check[p]:    # 방문한 적이 없는 사람이라면
            dfs(p,p2,count) # 그 사람과 관계를 맺고있는 사람 확인

dfs(p1,p2,0)
if not find:
    print(-1)