# 1. 회의 끝나는 시각 순서로 sorting
# 2. 순차적으로 확인
#   if (prevEnd ≤ nextStart) : prevEnd 업데이트 & cnt +1 & 다음 케이스
#   else : 다음 케이스

N = int(input())    # 회의 예약수
schedule = []       # 예약 테이블
cnt = 0

# 회의 일정 초기화
for i in range(N):
    start, end = map(int, input().split())
    schedule.append([start,end])

# 회의 끝나는 시각 순서로 sorting
for i in range(N):
    for j in range(i+1, N, +1):
        if schedule[i][1] > schedule[j][1]:
            s = schedule[i][0]
            e = schedule[i][1]
            schedule[i][0] = schedule[j][0]
            schedule[i][1] = schedule[j][1]
            schedule[j][0] = s
            schedule[j][1] = e

# 순차적으로 확인
prevEnd = 0
for i in range(N):
    nextStart = schedule[i][0]
    if prevEnd <= nextStart :
        prevEnd = schedule[i][1]
        cnt += 1

print(cnt)
