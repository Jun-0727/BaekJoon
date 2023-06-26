# 방법_1
# 축적 거리(accDist)를 이용하는 개념
# 출발도시 기름 가격(current)과 다음도시의 기름 가격(next)을 비교
# current ≥ next(더 싸면) : sum += current * accDist 하고 current 업데이트
# current < next(더 비싸면) : accDist에 해당 km만큼 추가

from sys import stdin

N = int(stdin.readline())
dist = list(map(int, stdin.readline().split()))
price = list(map(int, stdin.readline().split()))
sum = 0
update = True # 2중 for문을 해결한 key

# 현재 도시의 기름 가격(current)과 다음도시의 기름 가격(next)을 순차적으로 비교
for i in range(N-1):
    # 초기화하고 넘어갈지, 그대로 넘어갈지(next가 current보다 가격이 높다면)
    if update == True:
        current = price[i]
        accDist = dist[i]

    next = price[i+1]
    # next가 더 비싸면 그 다음 도시까지 가기 위한 거리 추가
    if current < next:
        accDist += dist[i+1]
        update = False
    # next가 더 저렴하면 (current * accDist)
    else:
        sum += current*accDist
        update = True
print(sum)


# 방법_2
# 런타임에러에 따른 해결방법
# 현재까지 가장 저렴한 기름가격을 currentPrice에 저장하는 개념.
# currentPrice vs nextPrice
# nextPrice가 더 비싸면 current 유지 / 더 싸면 current 업데이트
# 도시를 한번 이동할 때마다 currentPirce * dist[i]를 연산
# 이렇게하면 축적거리 변수에 대한 메모리를 사용하지 않음

update = True
sum = 0

for i in range(N-1):
    if update == True:
        current = price[i]

    next = price[i+1]

    if current < next:
        update = False
    else:
        update = True

    sum += current * dist[i]
print(sum)


# 근데 이렇게 할거면?
# 방법_3
sum = 0
cheapest = price[0]

for i in range(N-1):
    if cheapest > price[i]:
        cheapest = price[i]

    sum += cheapest * dist[i]
print(sum)


# 알게된 것
# 이중 for문
# 내부 for문에서 외부 for문의 조건(i)을 바꿀 수 없다
