# 가장 굵은 로프를 찾는다
# 가장 얇은 로프 * 로프의 갯수 구하고, 가장 얇은거 pop
# 끝까지 반복
"""
import sys
input = sys.stdin.readline

N = int(input())
ropes = [int(input()) for _ in range(N)]

candidates = [0]

for i in range(len(ropes)):
    weight = min(ropes) * len(ropes)
    
    if (weight > max(candidates)):
        candidates.append(weight)
    
    ropes.pop(ropes.index(min(ropes)))

print(max(candidates))
"""
# >> 시간 초과

# 매번 max(roeps)를 써서 로프를 찾지 말고, ropes를 sorting해서 가 아니라 위에서 부터 하나씩 꺼내자
import sys
input = sys.stdin.readline

N = int(input())
ropes = [int(input()) for _ in range(N)]
ropes = sorted(ropes)

candidates = [0]

for i in range(N):
    weight = ropes[i] * (N - i)
    
    if (weight > max(candidates)):
        candidates.append(weight)

print(max(candidates))

