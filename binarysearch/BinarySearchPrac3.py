'''
문제: 정렬된 배열에서 특정 수의 개수 구하기
N개의 원소를 포함하고 있는 수열이 오름차순으로 정렬되어 있다. 이때 이 수열에서 x가 등장하는 횟수를 계산하시오.
단, 이 문제는 시간 복잡도 O(logN)으로 알고리즘을 설계하지 않으면 시간 초과 판정을 받는다.

첫째 줄에 N(1 <= N <= 1,000,000)과 x(-10^9 <= x <= 10^9)가 정수 형태로 공백으로 구분되어 입력한다.
둘째 줄에 N개의 원소가 정수 형태로 공백으로 구분되어 입력한다.
''' 

from bisect import bisect_left, bisect_right
import sys

def count_by_range(array, num):
    right_index = bisect_right(array, num)
    left_index = bisect_left(array, num)
    result = right_index - left_index
    
    if result == 0:
        return -1
    
    return result

n, x = map(int, input().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

print(count_by_range(arr, x))