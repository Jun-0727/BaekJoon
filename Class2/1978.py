import sys
input = sys.stdin.readline

def check_prime_num(num):
    
    if num == 1 or num%2 == 0:
        return 0
    
    for i in range(3,num,2):
        if num%i == 0:
            return 0
    
    return 1

def solve(X):
    result = 0
    for x in X:
        result += check_prime_num(x)
    
    return print(result)

int(input())
candis = list(map(int, input().split()))
solve(candis)
