import sys
import heapq

input = sys.stdin.readline
N, K = map(int, input().split())

#--- 방법 1 ---#

# 1. gems, bags 리스트 생성
# 2. gems는 가격기준 최대힙, bags을 오름차순 정렬
# 3. gems 중 가장 비싼 보석을 꺼내서(pop)
# 4. 용량이 가장 작은 가방부터 꺼낸 보석을 넣어봄
# 5. 들어가면 해당 가방은 pop & 들어간 보석의 가격 계산
# 3~5 반복

# 보석 데이터 입력 받아서 리스트 생성
jewerly = []
for i in range(N):
    w,p= map(int, input().split())
    heapq.heappush(jewerly, (-1*p, w))

# 가방 데이터를 입력받아 리스트 생성 후 sorting
bags = [int(input()) for _ in range(K)]
bags.sort()

result = 0
# 가장 비싼 보석을 꺼내서 작은 가방에부터 차례대로 넣어서 들어가는 가방있으면 해당 가방 pop & result 연산
while(bags and jewerly):
    j = heapq.heappop(jewerly)     # 가장 비싼 보석 pop
    p, w = -1*j[0], j[1]           # 보석의 가격, 보석의 무게
    
    # 가장 작은 가방 부터 
    for i in range(len(bags)):
        # 보석을 넣을 수 있는 가방 찾은 후 pop
        if w <= bags[i]:
            print(bags)
            bags.pop(i)
            result += p
            break
print(result)
#--- 시간 초과 ---#


#--- 방법 2 ---#

# 1. gems, bags, values 리스트 생성
# 2. gems를 무게기준 최소힙에 구조로 저장, bags을 오름차순 정렬
# 3. bags 중 용량이 적은 가방부터 하나씩 꺼내서 확인
# 4. 가방에 들어갈 수 있는 보석을 gems 리스트에서 꺼내서(pop), value 리스트에 최대힙 구조로 넣음(push)
# 5. value 중 가장 비싼 보석을 꺼내서(pop) & 꺼낸 보석의 가격 계산
# 4~5 반복 : 이미 value에 들어가있는 보석은, 다음 가방에도 들어갈 수 있는 보석임

# 보석 데이터 입력 받아서 리스트 생성
gems = []
for i in range(N):
    w,p= map(int, input().split())
    heapq.heappush(gems, (w, p))

# 가방 데이터를 입력받아 리스트 생성 후 sorting
bags = [int(input()) for _ in range(K)]
bags.sort()

values = []
result = 0

# 용량이 적은 가방부터 하나씩 꺼내서 
for bag in bags:
    # [무게가 가장 적게 나가는 보석] ≤ [꺼낸 가방의 무게] 이면 
    # 보석의 가격을 value 리스트에 저장(push) & 꺼낸 보석을 리스트에서 제거(pop)
    while gems and gems[0][0] <= bag:
        tmp = heapq.heappop(gems)
        heapq.heappush(values, -tmp[1])
    
    # 현재까지 values 중 가장 큰 값을 꺼내서 result에 더함
    if values:
        result += -heapq.heappop(values)

print(result)
#--- 성공 ---#

# 최대힙
#   • heappush(list, -value)
#   • -heappop(list)

# 최소힙
#   • heappush(list, value) 
#   • heappop(list)

# 2차원 배열 정렬
#   - list.sort(key=lambda x:x[0])
#   - list.sort(key=lambda x:(x[1], x[0]))
# 