'''
문제 좌표 정렬 2
2차원 평면 위의 점 N개가 주어진다. 좌표를 y좌표가 증가하는 순으로, y좌표가 같으면 x좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성하시오.

첫째 줄에 점의 개수 N (1 ≤ N ≤ 100,000)이 주어진다. 
둘째 줄부터 N개의 줄에는 i번점의 위치 xi와 yi가 주어진다. (-100,000 ≤ xi, yi ≤ 100,000) 
좌표는 항상 정수이고, 위치가 같은 두 점은 없다.
'''

import sys

n = int(input())
data = []

for _ in range(n):
    input_data = sys.stdin.readline().rstrip().split()
    data.append((int(input_data[0]), int(input_data[1])))
    
data = sorted(data, key = lambda loc : (loc[1], loc[0]))

for loc in data:
    print(loc[0], loc[1])