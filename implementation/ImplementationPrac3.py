'''
문제: 왕실의 나이트
체스판은 8 X 8 좌표 평면이다. 체스판 특정한 한 칸에 나이트가 서 있다. 나이트는 L자 형태로만 이동할 수 있다.
나이트는 특정한 위치에서 다음과 같은 2가지 경우로 이동할 수 있다.

    1. 수평으로 두 칸 이동한 뒤에 수직으로 한 칸 이동하기
    2. 수직으로 두 칸 이동한 뒤에 수평으로 한 칸 이동하기

이처럼 8 X 8 좌표 평면상에서 나잍의 위치가 주어졌을 때 나이트가 이동할 수 있는 경우의 수를 출력하는 프로그램을 작성하시오.
이때 행 위치는 1부터 8로 표현하고, 열 위치는 a부터 h로 표현한다.

첫째 줄에 8 X 8 좌표 평면상에서 현재 나이트가 위치한 곳의 좌표를 나타내는 두 문자로 구성된 문자열이 입력된다. ex) a1, c2, g8
'''

input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1
count = 0

# 나이트가 이동할 수 있는 8가지 방향
steps = [(-1, -2), (1, -2), (-1, 2), (1, 2), (-2, -1), (-2, 1), (2, -1), (2, 1)]

# 나이트의 이동 수행
for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]
    
    # 나이트가 체스판을 벗어나지 않을 경우 count 증가
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        count += 1
        
print(count)