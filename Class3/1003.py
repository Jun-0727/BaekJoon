# 피보나치 함수 
# 0, 1 호출갯수 구하기
# 각각 메모이제이션
"""
import sys
input = sys.stdin.readline

def count(n):
    zero = [1,0]
    one = [0,1]

    for i in range(n-1):
        zero.append(zero[i] + zero[i+1])
        one.append(one[i] + one[i+1])
    
    li =[zero[n], one[n]]
    return li


N = int(input())
result = []

for _ in range(N):
    n = int(input())
    result.append(count(n))

for x in result:
    print(*x)
"""

import sys
input = sys.stdin.readline

def count(n):
    arr = [[1,0], [0,1]]

    for i in range(n-1):
        arr.append([
            arr[i][0]+arr[i+1][0] , arr[i][1]+arr[i+1][1]
        ])

    return arr[n]


T = int(input())
results = []

for i in range(T):
    n = int(input())
    results.append(count(n))

for result in results:
    print(*result)