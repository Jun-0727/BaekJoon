# 1. 동전의 가치를 sorting
# 2. K를 (가치가 가장 큰 동전)으로 나눈 몫과 나머지 계산 
#    몫: 필요한 동전 개수
#    나머지를 (그 다음으로 가치가 가장 큰 동전)으로 몫과 나머지 계산

N, K = map(int, input().split())    # N과 K를 공백으로 구분하여 입력 (N : 동전의 종류, K : 목표값 )
A = []      # 동전의 가치를 저장할 배열
cnt = 0     # 필요한 동전의 개수

for i in range(N):
    A.append(int(input()))  # 배열(리스트)에 값을 추가

for i in range(N-1, 0, -1):    # 가치가 큰 동전부터 K값과 비교하여 계산
    if K == 0:
        break
    else:
        cnt = cnt + K//A[i]
        K = K%A[i]

print(cnt)