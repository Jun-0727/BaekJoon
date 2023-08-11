import sys

input = sys.stdin.readline

N,M = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    tmp = [A[i][j] + B[i][j] for j in range(M)]
    print(*tmp)
