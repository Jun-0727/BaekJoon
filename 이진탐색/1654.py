import sys
input = sys.stdin.readline

K, N = map(int, input().split())
lans = [int(input()) for _ in range(K)]
start, end = 1, max(lans)

while start <= end :
    mid = (start+end)//2

    sum = 0
    for lan in lans:
        sum += lan//mid
        
    if sum < N:
        end = mid-1
    elif sum >= N:
        start = mid+1

print(end)