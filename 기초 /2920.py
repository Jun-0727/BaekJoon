# 음계
import sys
input = sys.stdin.readline

def func(array):
    if array[0] == 1:
        for i in range(7):
            if array[i] < array[i+1]:
                continue
            else :
                return print("mixed")
        return print("ascending")
    
    elif array[0] == 8:
        for i in range(7):
            if array[i] > array[i+1]:
                continue
            else :
                return print("mixed")
        return print("descending")
    
    else:
        print("mixed")

            
arr = list(map(int, input().split()))
func(arr)