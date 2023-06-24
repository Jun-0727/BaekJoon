# 1. 돈을 인출하는데 걸리는 시간을 오름차순으로 sorting
# 2. 차곡차곡 더해(sum & total)
import sys

N = int(sys.stdin.readline())
P = list(map(int, sys.stdin.readline().split()))
P.sort()

add = 0
sum = 0
for i in range(N):
    add += P[i]
    sum += add
print(sum)


"""
sum = 0
for i in range(n):
    sum += time.pop() * (i+1)
print(sum)                 

"""