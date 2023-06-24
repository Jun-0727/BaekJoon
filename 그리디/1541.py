"""
state : +연산 OR -연산 --> negative
1. +가 나오면, negative 확인 후 + OR - 연산 
2. -가 나오면, negative 확인 후
   negative = true 인 경우 - 연산
   negatice = false 인 경우 + 연산 후, negative = True
3. 문자열 끝에 오면 state 확인 후 + OR - 연산
"""
import sys

exp = sys.stdin.readline()

negative = False
checkPoint = 0
sum = 0

# expression을 순차적으로 읽음
for i in range(len(exp)):
    # operator가 '+'인 경우
    if exp[i] == "+":
        operand = int(exp[checkPoint:i])
        checkPoint = i+1

        if negative == True:
            sum -= operand
        else:
            sum += operand
            
    # operator가 '-'인 경우
    if exp[i] == "-":
        operand = int(exp[checkPoint:i])
        checkPoint = i+1

        if negative == True:
            sum -= operand
        else:
            sum += operand
            negative = True
        
    # expression의 마지막 숫자 처리
    if i == len(exp)-1:
        operand = int(exp[checkPoint:])

        if negative == True:
            sum -= operand
        else:
            sum += operand

print(sum)
