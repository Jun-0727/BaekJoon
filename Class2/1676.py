import sys
input = sys.stdin.readline

def factorial(num):
    result = 1 
    for i in range(1,num+1):
        result *= i
    return result

def solve(num):
    count = 0
    while True:
        if num % 10 == 0:
            num = num // 10
            count += 1
        else:
            break
    
    return print(count)

solve(factorial(int(input())))