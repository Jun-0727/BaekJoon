# 가방을 무게별 오름차순으로 sorting
# 가장 비싼 보석의 index를 구함
# weight = 보석[index][0] & value = 보석[index][1] , pop
# for i in range(가방) : 가능한 가장 비싼 보석을 가장 가벼운 가방에 넣음

from sys import stdin

N, K = map(int, stdin.readline().split())
weight = []
price = []
bag = []

for i in range(N):
    M, V = map(int, stdin.readline().split())
    weight.append(M)
    price.append(V)

for i in range(K):
    bag.append(int(stdin.readline()))

bag.sort()
sum = 0

# 남은 가방 and 보석이 있다면
while(len(bag) > 0 and len(price) > 0 ):
    
    # 가장 비싼 보석
    index = price.index(max(price))

    # 가장 비싼 보석의 무게와 가격을 변수에 저장한 후 그 보석을 리스트에서 제외
    curWeight = weight[index]
    curPrice = price[index]

    weight.pop(index)
    price.pop(index)

    # 무게가 가장 작은 가방부터 순차적으로 확인
    for i in range(len(bag)):

        # 가방에 담을 수 있으면 담고 next
        if bag[i] >= curWeight:
            sum += curPrice
            bag.pop(i)
            break

print(sum)