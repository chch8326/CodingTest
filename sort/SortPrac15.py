'''
문제: 좌표 압축
수직선 위에 N개의 좌표 X1, X2, ..., XN이 있다. 이 좌표에 좌표 압축을 적용하려고 한다.
Xi를 좌표 압축한 결과 X'i의 값은 Xi > Xj를 만족하는 서로 다른 좌표의 개수와 같아야 한다.
X1, X2, ..., XN에 좌표 압축을 적용한 결과 X'1, X'2, ..., X'N를 출력해보자.

첫째 줄에 N이 주어진다.
둘째 줄에는 공백 한 칸으로 구분된 X1, X2, ..., XN이 주어진다.
'''

import sys

n = int(sys.stdin.readline().rstrip())
data = list(map(int, sys.stdin.readline().rstrip().split()))

# data 리스트의 중복 요소를 set으로 제거하면서 리스트화 및 정렬
arr = sorted(list(set(data))) 

# 요소의 인덱스가 한 요소보다 작은 요소의 수가 됨
dic = {arr[i] : i for i in range(len(arr))} 

for i in data:
    print(dic[i], end = ' ')