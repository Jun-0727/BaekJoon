# 1) A를 sorting 하고
# 2) B[i]중 가장 큰 값의 index를 찾아서, C[index]에 A의 최소값을 넣고
# 3) 위에서 찾은 index제외 후 나머지 중 (2)번 수행 

from sys import stdin

N = int(input())
A = list(map(int, stdin.readline().split()))
B = list(map(int, stdin.readline().split()))
C = [0 for i in range(N)]
D = [0 for i in range(N)]

A.sort()
sum = 0
for i in range(N):
    D[i] = B[i]

for i in range(N):
    max = 0
    for j in range(N):
        if max < D[j]:
            max = D[j]
            index = j

    D[index] = 0
    C[index] = A[i]

for i in range(N):
    sum += B[i]*C[i]
print(sum)

# 이건 아무리봐도 아니지...
# 위의 기능과 유사 기능을하는 pop이라는 친구



sum = 0
A.sort()
for i in range(N):
    sum += A[i] * max(B)
    B.pop(B.index(max(B)))
print(sum)

# 알게된 것
# list.pop(i) : 배열 중 index가 i인 원소의 값을 꺼내온 뒤 그 원소 삭제
# list.index(max(list)) : 배열 중 값이 최대/최소인 원소의 index 가져옴