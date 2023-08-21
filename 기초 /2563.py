N = int(input())

graph = [[False]*100 for _ in range(100)]

for _ in range(N):
    x, y = map(int, input().split())
    for i in range(x,10+x):
        for j in range(y,10+y):
            if not graph[i][j]:
                graph[i][j] = True

result = 0
for i in range(100):
    result += sum(graph[i])
print(result)