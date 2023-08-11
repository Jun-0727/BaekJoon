"""
# Hello World 출력하기
print('Hello World')
print("Hello World")

# 'Hello Wolrd' 출력하기
print("'Hello World'")
print("\'Hello World\'")
print('\'Hello World\'')

# "Hello World" 출력하기
print('"Hello World"')
print('\"Hello World\"')
print("\"Hello World\"")

#6
print("\"!@#$^&*()\'")

#7
print("\"C:\Download\\'hello'.py\"")

#8
print("print(\"Hello\\nWorld\")")

# 9 : 입력
# 입력 함수 :input()
ch = input("문자 1개 입력하기 :")
print(ch)

# 10
# 문자열 정수로 바꾸기 : int(n)
ch = input("정수 1개 입력하기 : ")
i = int(ch)
print(i)

# 11
# 문자열 실수로 바꾸기 : float(n)
str = input("실수 1개 입력하기 : ")
f = float(str)
print(str)

# 12
ch1 = input()
ch2 = input()
a = int(ch1)
b = int(ch2)
print(a)
print(b)

# 13
# input().split() : 공백으로 구분
ch1, ch2 = input().split()
print(ch2)
print(ch1)

#14
str = input()
a = float(str)

for i in range(0,3,1) :
    print(a)

# 15
a, b = input().split()
a = int(a)
b=int(b)
print(a)
print(b)

# 16
str1, str2 = input().split()
print(str2, str1)

# 17
s = input()
print(s,s,s)


# 18
h, m = input().split()
h = int(h)
m = int(m)
print( "%d : %d" % (h,m))

h, m, s = input().split(':')
print(h,m,s, sep=':') 

# 19
year, month, day = input("yyyy.mm.dd 입력 : ").split('.')
print(day, month, year, sep='-')

# 20 주민번호 입력하기
idNumFront, idNumBack = input("주민번호를 입력하시오(yymmdd-xxxxxxx)").split('-')
print(idNumFront+idNumBack)

# 21 : 입력받은 단어 한글자씩 출력하기
# 1.문자열은 배열이다!
# 2.문자열 길이 반환 : len()
str = input()
for i in range(0, len(str), 1) :
    print(str[i])

# 22 : 부분 출력하기
# s[n:m] --> 배열의 n번 ~ m-1번 까지 
s = input()
print(s[0:2],s[2:4],s[4:6])

# 23 : 시:분:초 입력받아 분만 출력하기
h, m, s = input("시분초 입력(hh:mm:ss) : ").split(':')
print(m)

# s = input()
# print(s[3:5])

# 24 : 문자 이어붙이기
s1,s2 = input("두 단어를 공백으로 구분하여 입력 : ").split()
print(s1+s2)

# 25 : 정수 2개 입력받아 합 계산하기
a, b = input("정수 2개를 공백으로 구분하여 입력 : ").split()
sum = int(a) + int(b)
print(sum)

# 26 : 실수 2개 입력받아 합 계산하기
a, b = input("실수 2개를 공백으로 구분하여 입력 : ").split()
sum = float(a) + float(b)
print(sum)

# 27 : 10진수 정수 입력받아 16진수 소문자로 출력하기
s = input("10진수 정수를 입력 : ")
i = int(s)
print("%x" % (i))

# 28 : 10진수 정수 입력받아 16진수 대문자로 출력하기
s = input("10진수 정수를 입력 : ")
i = int(s)
print("%X" % (i))

# 29 : 16진수를 입력받아 8진수로 출력
# 16진수로 바꾸기 : int(n, 16)
s = input("16진수 입력 : ")
x = int(s, 16)
print("%o" % (x))

# 30 : 영문자를 유니코드로 변환하기
# 문자 --> 정수값 : ord()  
# ordinal position 의 약자
s = ord(input("문자 한개 입력 : "))
print(s)

# 31 : 정수를 유니코드로 변환하기
# 정수값 --> 문자 : chr()
s = input("정수 입력 : ")
i = int(s)
c = chr(i)
print(c)

# 32 : 정수 부호바꾸기
i = int(input("정수입력 : "))
print(-i)

# 33 : 다음문자 출력
s = input("문자입력 : ")
i = ord(s)
print(chr(i+1))

# 34 : 뺄셈
a, b = input("정수 두 개 공백으로 구분 : ").split()
a = int(a)
b = int(b)
sub = a - b 
print(sub)

# 35 : 곱셈
a, b = input("실수 두 개 공백으로 구분 : ").split()
a = float(a)
b = float(b)
mul = a*b
print(mul)



# 36 : 단어 반복출력
# 문자열 * 정수 -> 정수 만큼 반복하여 출력
w, n = input("단어와 반복횟수 공백으로 구분하여 입력 : ").split()
cnt = int(n)
print(w*cnt)


# 37 : 문장 반복출력
n = input("반복횟수 입력 : ")
cnt = int(n)
s = input("문장 입력")
print(s*cnt)



# 38 : 거듭제곱 - 정수편
# 거듭제곱 연산자 : **
a, b = input("정수 2개 공백구분 입력 : ").split()
a = int(a)
b = int(b)
print(a**b)

# 39 : 거듭제곱 - 실수편
a, b = input("실수 2개 공백구분 입력 : ").split()
a = float(a)
b = float(b)
print(a**b)

# 40 : 정수 2개 입력받아 나눈 몫 계산하기
a, b = input("정수 2개 공백구분 입력 : ").split()
a = int(a)
b = int(b)
print(a//b)

# 41 : 정수 2개 입력받아 나눈 나머지 계산하기
a, b = input("정수 2개 공백구분 입력 : ").split()
a = int(a)
b = int(b)
print(a%b)

# 실수로 나누면?
a, b = input("실수 2개 공백구분 입력 : ").split()
a = float(a)
b = float(b)
print(a%b)

# 42 : 실수 1개 입력받아 소숫점이하 자리 변환
# 반올림 해주는 함수 : format(실수, ".2f" ) - 2번째 자리까지의 정확도 = 3번째에서 반올림함
f = input("실수 한개 입력 : ")
f = float(f)
print(format(f, ".2f"))

# 43 : 실수 2개 입력받아 나눈 결과 계산
a, b = input("실수 2개 공백구분 입력 : ").split()
a = float(a)
b = float(b)
print(format(a/b, ".3f"))

# 44 : 정수 2개 입력받아 자동 계산
a, b = input("정수 2개 공백구분 입력 : ").split()
a = int(a)
b = int(b)
print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)
print(format(a/b, ".2f"))

# 45 : 정수 3개 입력받아 합과 평균 출력
# 반올림 해주는 함수2 : round(숫자, 숫자)
# 사사오입 원칙 : 반올림할 자리의 수가 5이면 반올림 할 때, 앞자리의 숫자가 짝수면 내림 / 홀수면 올림
a, b, c = input("정수 3개 공백구분 입력 : ").split()
a = int(a)
b = int(b)
c = int(c)
sum = a+b+c
print(sum, format(sum/3, ".2f"))
print(sum, round(sum/3, 2))

# 46 : 정수 1개 입력받아 2배 곱해 출력 - 비트시프트연산 사용
# Python에서는 실수의 비트시프트연산은 허용하지 않는다
n = input("정수 1개 입력 : ")
n = int(n)
print(n<<1)

# 47 : 2의 거듭제곱 배로 곱해 출력 - 비트시프트 연산 사용
a, b = input("정수 2개 입력 : ").split()
a = int(a)
b = int(b)
print(a<<b)

# 48 : 정수 2개 입력받아 비교하기1
a, b = input("정수 2개 입력 : ").split()
a = int(a)
b = int(b)
print(a<b)

# 49 : 정수 2개 입력받아 비교하기2
a, b = input("정수 2개 입력 : ").split()
a = int(a)
b = int(b)
print(a==b)

# 50 : 정수 2개 입력받아 비교하기3
a, b = input("정수 2개 입력 : ").split()
a = int(a)
b = int(b)
print(a<=b)
 
# 51 : 정수 2개 입력받아 비교하기4
a, b = input("정수 2개 입력 : ").split()
a = int(a)
b = int(b)
print(a!=b)

# 52 : 정수 입력받아 참 거짓 평가하기 - bool()
# bool() 함수 : 0이면 False, 나머지는 True
a = input("정수 1개 입력 : ")
a = int(a)
print(bool(a))

# 53 : 참 거짓 바꾸기 - not
# bool 값 반대 출력 : not a
a = bool(int(input("정수 1개 입력 : ")))
print(not a)

# 54 : 둘 다 참일 경우만 참 출력하기 - and
a, b = input("정수 2개 입력 : ").split()
a = int(a)
b = int(b)
print(bool(a) and bool(b))

# 55 :하나라도 참이면 참 출력하기 - or
a, b = input("정수 2개 입력 : ").split()
a = int(a)
b = int(b)
print(bool(a) or bool(b))

# 56 : 참/거짓이 서로 다를 때에만 참 출력하기 - xor
a, b = input("정수 2개 입력 : ").split()
a = bool(int(a))
b = bool(int(b))
print( (a and not b) or (not a and b))

# 57 : 참/거짓이 서로 같을 때에만 참 출력하기
a, b = input("정수 2개 입력 : ").split()
a = bool(int(a))
b = bool(int(b))
print(a==b)

# 58 : 둘 다 거짓일 경우만 참 출력하기
# not A and not B = not(A or B)
a, b = input("정수 2개 입력 : ").split()
a = bool(int(a))
b = bool(int(b))
print( not (a or b))

# 59 : 비트단위로 NOT 하여 출력하기
# 비트단위 연산자
# ~  : not 
# &  : and
# |  : or 
# ^  : xor
# << : left shift
# >> : right shift
a = int(input("정수 1개 입력 : "))
print(~a)

# 60 : 비트단위로 AND 하여 출력하기
# 네트워크에 연결되어 있는 두 개의 컴퓨터가 데이터를 주고받기 위해 같은 네트워크에 있는지 아닌지를 판단하는데 사용된다.
a, b = input("정수 2개 입력 : ").split()
a = int(a)
b = int(b)
print(a&b)

# 61 : 비트단위로 OR 하여 출력하기
a, b = input("정수 2개 입력 : ").split()
a = int(a)
b = int(b)
print(a|b)

# 62 : 비트단위로 XOR 하여 출력하기
# 두 장의 이미지가 겹쳐졌을 때 색이 서로 다른 부분만 처리할 수 있다.  ex) 비행기 슈팅게임
a, b = input("정수 2개 입력 : ").split()
a = int(a)
b = int(b)
print(a^b)

# 63 : 정수 2개 입력받아 큰 값 출력하기
# 3항 연산 : a if (a>=b) else b)
a, b = input("정수 2개 입력 : ").split()
a = int(a)
b = int(b)
print(max(a,b))

# 64 : 정수 3개입력받아 가장 작은 값 출력하기
a, b, c = input("정수 3개 입력 : ").split()
a = int(a)
b = int(b)
c = int(c)
print(min(a,b,c))

# 65 : 정수 3개 입력받아 짝수만 출력하기
a, b, c = input("정수 3개 입력 : ").split()
a = int(a)
b = int(b)
c = int(c)

if(a%2 == 0) :
        print(a)
if(b%2 == 0) :
        print(b)
if(c%2 == 0) :
        print(c)        

# 63 : 정수 3개 입력받아 짝/홀 출력하기
a, b, c = input("정수 3개 입력 : ").split()
a = int(a)
b = int(b)
c = int(c)

if(a%2 == 0) :
        print("even")
else :
        print("odd")

if(b%2 == 0) :
        print("even")
else :
        print("odd")

if(c%2 == 0) :
        print("even") 
else :
        print("odd")

# 67 : 정수 1개 입력받아 분류하기
a = int(input("정수 1개 입력 : "))
if a < 0 :
    if a%2 == 0 :
        print("A")
    else :
        print("B")
else :
    if a%2 == 0 :
        print("C")
    else :
        print("D")

# 68 : 점수 입력받아 평가 출력하기
score = int(input("정수 1개 입력 : "))
if score >= 90 :
    print("A")
elif score >= 70 : 
    print("B")
elif score >= 40 :
    print("C")
else :
    print("D")

# 69 : 평가 입력받아 다르게 출력하기
eval = input("평가 입력(A/B/C/D 중 하나) : ")
if eval == "A" :
    print("best!!!")
elif eval == "B" :
    print("good!!")
elif eval == "C" :
    print("run!")
elif eval == "D":
    print("slowly~")
else : 
    print("what?")

# 70 : 월 입력받아 계절 출력하기
month = int(input("월 입력(1~12) : "))
if month//3 == 1 :
    print('spring')
elif month//3 == 2 :
    print("summer")
elif month//3 == 3 :
    print("fall")
else :
    print("winter")

# 71 : 0 입력될 때까지 무한 출력하기
n = 1
while n != 0 :
    n = int(input("정수 1개 입력 : "))
    if n != 0 :
        print(n)
    else :
        break

# 72 : 정수 1개 입력받아 카운트다운 출력하기1
n = int(input("정수 1개 입력 : "))

for i in range(n,0,-1) :
    print(i)

# 73 : 정수 1개 입력받아 카운트다운 출력하기2
n = int(input("정수 1개 입력 : "))

for i in range(n,-1,-1) :
    print(i)

# 74 : 문자 1개 입력받아 알파벳 출력하기
c = ord(input("문자 1개 입력(a~z): "))

for i in range(97, c+1, 1) :
    print(chr(i))

# 75 : 정수 1개 입력받아 그 수까지 출력하기1
n = int(input("정수 1개 입력 : "))
for i in range(0,n+1,1) :
    print(i)

# 76 : 정수 1개 입력받아 그 수까지 출력하기2
# range(n) : 0, 1, ... , n-1 까지의 수열을 의미
# range(끝)
# range(시작, 끝)
# ragne(시작, 끝, 증감)
#
n = int(input("정수 1개 입력 : "))
for i in range(0,n+1,1) :
    print(i)

# 77 : 짝수 합 구하기
n = int(input("정수 1개 입력 : "))
sum = 0
for i in range(0, n+1, 1) :
    if( i%2 == 0 ) :
        sum += i
print(sum)

# 78 : 원하는 문자가 입력될 때까지 반복 출력하기
while 1 :
    s = input("문자 입력 : ")
    if s != 'q' :
        print(s)
    else :
        break 

# 79 : 언제까지 더해야 할까?
n = int(input("정수 1개 입력 : "))
sum = 0
cnt = 1

while sum < n :
    sum += cnt
    cnt += 1

print(cnt-1)

# 80 : 주사위 2개 던지기
n, m = input("정수 2개 입력 : ").split()
n = int(n)
m = int(m)

for i in range(1,n+1) :
    for j in range(1,m+1) :
        print(i,j)

# 81 : 16진수로 구구단 출력하기
# %x는 소문자 16진수, %X로 출력하면 대문자 16진수로 출력한다
# %o는 소문자 8진수, %O로 출력하면 대문자 8진수로 출력한다
# % 출력 방법은 "%X"%n.  X는 16진수를 뜻하고 n은 변수를 뜻한다.
# 16, 8 진수를 입력받을 때는 int(n,16) , int(n,8)을 이용한다.

n = input("16진수 입력 : ")
n = int(n, 16)

for i in range(1,16,1) :
    print('%X'%n, '*%X'%i, '=%X'%(n*i), sep='')

# 82 : 369 게임
# print()의 옵션으로 end="" 와 sep=""가 있다.
# end는 끝날때, sep는 콤마(,)마다 입력되는 값이다.
n =  int(input("정수 1개 입력 : "))

for i in range (1, n+1) :
    if i%10 == 3 or i%10 == 6 or i%10 == 9 :
        print("X", end=' ')
    else :
        print(i, end=' ')

# 83 : 빛 섞어 색 만들기
r, g, b = input("정수 3개 입력 : ").split()
r = int(r)
g = int(g)
b = int(b)

for i in range(0,r) :
    for j in range(0, g) :
        for k in range(0, b) :
            print(i, j, k)
print(r*g*b)

# 84 : 소리 파일 저장용량 계산하기
# 반올림 계산 함수 복습 - round()
h, b, c, s = input("정수 4개 입력 : ").split()

h = int(h)
b = int(b)
c = int(c)
s = int(s)

print(round(h*b*c*s/8/1024/1024, 1), "MB")

# map() 사용법
# map(function, iterable))
# function - 함수 / iterable - 반복가능한 자료형
# ex) h,b,c,s = map(int,input().split())
# m = (h* b * c * s)/8/1024/1024
# print('%.1f MB' %m)

# 85 : 그림 파일 저장용량 계산하기
w, h, b = map(int, input("정수 3개 입력 : ").split())

print(round(w*h*b/8/1024/1024, 2), "MB")

# 86 : 거기까지! 이제 그만
n = int(input("정수 1개 입력 : "))
sum = 0
cnt = 1
while sum < n :
    sum += cnt
    cnt += 1
print(sum)

# 87 : 3의 배수는 통과
n = int(input("정수 1개 입력 : "))

for i in range(1, n+1) :
    if i%3 == 0 :
        continue
    print(i, end=' ')

# 88 : 수 나열하기1 - 등차수열
a, d, n = map(int, input("정수 3개 입력 : ").split())

print(a+(d*(n-1)))

# 89 : 수 나열하기2 - 등비수열
a, r, n = map(int, input("정수 3개 입력 : ").split())

print(a*(r**(n-1)))

# 90 : 수 나열하기3 - 규칙
a, m, d, n = map(int, input("정수 4개 입력 : ").split())
k = a
for i in range(2,n+1) :
    k = k * m + d
print(k)

# 91 : 함께 문제 푸는 날
a, b, c = map(int, input("정수 3개 입력 : ").split())
day = 1

while day%a != 0 or day%b != 0 or day%c != 0 :
    day += 1

print(day)

# 92 : 이상한 출석 번호 부르기1
# a가 부른걸 의미하는 거구나;;; 수동 랜덤이네
n = int(input())
a = list(map(int,input().split()))

d = [0] * 24

for i in range(n) :
    d[a[i]] += 1

for i in range(1, 24):
    print(d[i], end=' ')

# 93 : 이상한 출석 번호 부르기2
n = int(input())
a = list(map(int, input().split()))

for i in range(n-1, -1, -1) :
    print(a[i], end=' ')

# 94 : 이상한 출석 번호 부르기3
n = int(input())
a = list(map(int, input().split()))

print(min(a))

# 95 : 바둑판에 흰 돌 놓기
# 2차원 배열 초기화하기 : arr = [[0]*n for _ in range(m)]

b = [[0]*19 for _ in range(19)]

n = int(input("놓을 돌의 개수 : "))
for i in range(n) :
    x, y = map(int, input().split())
    b[x][y] = 1
    
for i in range(19) :
    for k in range(19) :
        print(b[i][k], end=' ')
    print()

# 96 : 바둑알 십자 뒤집기
b = [[0]*20 for _ in range(20)]

for i in range(1,20) :
    a = list(map(int, input().split()))
    for j in range(1,20) :
        b[i][j] = a[j-1]

n = int(input("선택할 좌표 갯수 : "))

for i in range(n):
    x, y = map(int, input("좌표 선택 : ").split())
    for j in range(1,20):
        if b[j][y] == 0 :
            b[j][y] = 1
        else :
            b[j][y] = 0 
    
    for k in range(1,20) :
        if b[x][k] == 0 :
            b[x][k] = 1
        else :
            b[x][k] = 0
                        
for i in range(1,20) :
    for j in range(1,20) :
        print(b[i][j], end=' ')
    print()

# 97 : 설탕과자 뽑기
# x축이 세로, y축이 가로 인 문제였음..
h, w = map(int, input("세로, 가로 : ").split())
n =  int(input("막대의 개수 : "))

board = [[0]*h for _ in range(w)]
for i in range(n) :
    l, d, x, y = map(int, input("길이, 방향, 좌표(x,y)").split())
    x = x-1
    y = y-1

    for j in range(l):
        if d == 0 :
            board[y+j][x] = 1
        else :
            board[y][x+j] = 1

for i in range(h) :
    for j in range(w):
        print(board[j][i], end=' ')
    print()

"""

# 98 : 성실한 개미
box = [[0]*10 for _ in range(10)]
    
for i in range(10):
    r = list(map(int, input().split()))
    for j in range(10) :
        box[j][i] = r[j]

print()
for i in range(10) :
    for j in range(10):
        print(box[j][i], end=' ')
    print()
print()
x, y = 1, 1

while True :
    if box[x+1][y] == 0 :
        box[x][y] = 9
        x += 1            
        
    elif box[x+1][y] == 1 :
        box[x][y] = 9
        if box[x][y+1] == 1 :
            break
        else :
            y += 1
    
    if box[x][y] == 2 :
        box[x][y] = 9
        break

for i in range(10) :
    for j in range(10):
        print(box[j][i], end=' ')
    print()
