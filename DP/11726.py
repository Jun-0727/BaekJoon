# 2xn 타일링
# 2x1 일때 / 2x2 일때 / 2x3 일때 / 2x4 일때/ 2x5 ... 규칙나옴

import sys
input = sys.stdin.readline

def solution(n):
    arr = [0,1,2]

    for i in range(3, n+1):
        arr.append(arr[i-2]+arr[i-1])
    
    return arr[n]

n = int(input())
print(solution(n)%10007)