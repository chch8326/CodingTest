'''
문제: 고정점 찾기
고정점이란 수열의 원소 중에서 그 값이 인덱스와 동일한 원소를 의미한다. 하나의 수열이 N개의 서로 다른 원소를 포함하고 있으며,
모든 원소가 오름차순으로 정렬되 있을 때, 이 수열에서 고정점이 있다면 고정점을 출력하는 프로그램을 작성하시오.
고정점은 1개만 존재하며 고정점이 없다면 -1을 반환한다. 단, 이 문제는 시간 복잡도 O(logN)으로 알고리즘을 설계하지 않으면 시간 초과 판정을 받는다.

첫째 줄에 N(1 <= N <= 1,000,000)이 입력된다.
둘째 줄에 N개의 원소가 정수 형태로 공백으로 구분되어 입력된다.
''' 

from bisect import bisect_left
import sys

def fixed_point(arr):
    for i in range(len(arr)):
        index = bisect_left(arr, arr[i])
        
        if index == arr[i]:
            return arr[i]
        
    return -1

n = int(input())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

print(fixed_point(arr))