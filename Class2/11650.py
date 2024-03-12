import sys
input = sys.stdin.readline

N = int(input())
location = []
for _ in range(N):
    location.append(list(map(int, input().split())))

location.sort()
for x in location:
    print(*x)