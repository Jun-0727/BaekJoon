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

# 알게된 것
# 공백을 구분점으로 데이터를 저장하는 것
# list(map(int, input().split()))
# 처음에 리스트 두개 놓고 하나에 append로 초기화 시키고, int 타입으로 바꿔서 다른 리스트에 저장