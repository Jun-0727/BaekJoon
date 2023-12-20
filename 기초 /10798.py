# 밑에 두줄 추가하면 답이 달라짐 WHY??
# import sys
# input = sys.stdin.readline


words = [input() for _ in range(5)]
for i in range(15):
    for j in range(5):
        if i < len(words[j]):
            print(words[j][i], end='')



"""
words1 = [list(input()) for _ in range(5)]
wordw2 = [input() for _ in range(5)]
nums1 = [list(map(int, input())) for _ in range(5)]
nums2 = [list(map(int, input().split())) for _ in range(5)]
"""