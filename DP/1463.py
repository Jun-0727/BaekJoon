# 1로 만들기
# DP : 작은 문제가 반복 / 같은 문제는 답이 같다
# Memoization
# 1~10 해보면 보임

import sys
input = sys.stdin.readline

# arr[n/3] vs arr[n/2] vs arr[n-1]
def solution(n):
    arr = [0,0,1,1]

    for i in range(4,n+1):
        if i%6==0:
            arr.append(min(arr[i//3], arr[i//2], arr[i-1])+1)
       
        elif i%3 == 0:
            arr.append(min(arr[i//3], arr[i-1])+1)
        
        elif i%2 == 0:
            arr.append(min(arr[i//2], arr[i-1])+1)
        
        else :
            arr.append(arr[i-1]+1)
    
    return arr[n]

n = int(input())
print(solution(n))
