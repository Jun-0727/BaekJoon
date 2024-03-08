import sys
input = sys.stdin.readline


def solve(array):
    start = 1
    end = max(array)
    
    while start <= end:
        mid = (start+end)//2
        
        sum = 0
        for x in array:
            if x-mid > 0:
                sum += x-mid
        
        if sum >= M:
            start = mid+1
        else:
            end = mid-1
    
    return print(end)

N, M = map(int, input().split())
trees = list(map(int, input().split()))

solve(trees)

