
"""
# 알파벳 딕셔너리 : A~J 
# 딕셔너리에 담겨있는 숫자를 확인
# 입력한 알파벳의 자릿수를 확인 - 높은 자릿수부터 차례대로 높은 숫자를 부여

"""
import sys

input = sys.stdin.readline

N = int(input())

# Try_1

alphaDict = {'A':0, 'B':0, 'C':0, 'D':0, 'E':0, 'F':0, 'G':0, 'H':0,'I':0, 'J':0}       # 딕셔너리 초기화
words = []      # 단어 리스트 초기화

# 단어 입력
for i in range(N):
    words.append(sys.stdin.readline())

# 각 단어의 알파벳 자릿수 확인
for i in range(N):
    for j in range(len(words[i])-1):
        alphabet = words[i][j]
        digit = 10**(len(words[i])-2 - j)

        if (alphaDict[alphabet] < digit): 
            alphaDict[alphabet] = digit

# 알파벳 딕셔너리를 내림차순으로 정렬
alphaDict = dict(sorted(alphaDict.items(), key = lambda item:item[1], reverse=True))

# 알파벳 딕셔너리의 내림차순 순서대로 9~0 부여
weight = 9
for key in alphaDict:
    alphaDict[key] = weight
    weight -= 1

print(alphaDict)
# 각 단어의 알파벳 번호와 자릿수를 곱해서 총합을 구함
sum = 0
for i in range(N):
    for j in range(len(words[i])-1):
        alphabet = words[i][j]
        digit = 10**(len(words[i])-2 - j)

        sum += alphaDict[alphabet] * digit
        print(sum)

print(sum)  

# 문제점 : 단어의 자리수를 확인하는데 너무 복잡한듯!



# Try_2

alphaDict = {'A':0, 'B':0, 'C':0, 'D':0, 'E':0, 'F':0, 'G':0, 'H':0,'I':0, 'J':0}
words = []

# 1. 단어 입력
for i in range(N):
    words.append(input())

# 2. 각 단어의 알파벳 자릿수 확인
for i in range(N):
    for j in range(len(words[i])-1):
        alphabet = words[i][j]
        digit = 10**(len(words[i])-2 - j)

        alphaDict[alphabet] += digit

# 3. 알파벳의 가중치를 내림차순으로 정렬
alphaDict = dict(sorted(alphaDict.items(), key = lambda item:item[1], reverse=True))

# 4. 알파벳 가중치에 따라 9~0 부여
weight = 9
result = 0
for key in alphaDict:
    result += alphaDict[key] * weight
    weight -= 1

print(result)

# 문제점 : 4번에서 예외가 발생 --> ABB, BA * 9 : B가 A보다 자릿수는 낮지만 빈도가 잦아서 총합이 더 큼

# 4번의 문제점을 해결하기 위해 높은 자릿수의 알파벳에 높은 숫자가 아닌 
# 가중치가 큰 알파벳에 높은 숫자를 부여하자!


# Try_3

N = int(input())
alphaDict = {}  # 딕셔너리 초기화

# 단어 입력
words = []      # 리스트 초기화
for _ in range(N):
    words.append(input())

# 하나의 단어씩 확인
for word in words:
    # 단어의 길이를 이용하여 10의 제곱수 설정
    squraeRoot = len(word)-1   
    for c in word:
        # 딕셔너리 설정(알파벳에 대응하는 가중치 업데이트)
        if c in alphaDict:
            alphaDict[c] += 10 ** squraeRoot
        else:
            alphaDict[c] = 10 ** squraeRoot
        
        squraeRoot -= 1

# 딕셔너리에서 알파벳의 가중치를 기준으로 내림차순
# alphaDict = dict(sorted(alphaDict.items(), key = lambda item:item[1], reverse=True))    
alphaDict = sorted(alphaDict.values(), reverse=True)

result = 0
num = 9

# 가중치가 큰 알파벳부터 9~1 를 곱한 뒤 총합 계산
for value in alphaDict:
    result += value * num
    num -= 1

print(result)

# 배운것
# Dictionary
# 1.CRUD 
#    Init   -> dict = {'A':0}  OR  dict = dict(A=0)
#    Create -> dic['newKey'] = 777
#    Read   -> dict['key']
#    Update -> dict['key'] = 0  OR  dict.update({'key':0})
#    Delete -> del dict['key']

# 2. 복사
#    얕은 복사 : dict.copy - 참조하는 주소가 같음. 즉 수정하면 둘다 바뀜
#    깊은 복사 : dict.deepcopy - 참조하는 주소가 다름. 즉 새로운 dictionary를 생성

# 3. for 문 
#    - for key in dict:     key값 할당
#    - for value in dict.values():     value값 할당
#    - for key, value in dict.items(): 둘 다 할당

# 4. in
#     - 'existKey' in dict    -> True
#     - 'nonExistKey' in dict -> False

# !!!dictionary는 순서가 없다!!!