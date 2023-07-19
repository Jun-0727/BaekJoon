"""
pay = int(input())
change = 1000
cnt = 0

change = 1000 - pay

while(change > 0):    
    if change >= 500:
        cnt += change//500
        change = change%500
    elif change >= 100:
        cnt += change//100
        change = change%100
    elif change >= 50:
        cnt += change//50
        change = change%50
    elif change >= 10:
        cnt += change//10
        change = change%10
    elif change >= 5:
        cnt += change//5
        change = change%5
    else:
        cnt += change
        change = 0

print(cnt)
"""

# 코드 이쁘게 작성하기
n = int(input())
n = 1000 - n

cnt = 0
for x in [500,100,50,10,5,1]:
    cnt += n//x
    n %= x

print(cnt)