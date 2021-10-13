'''
문제: 상하좌우
여행가 A는 N X N 크기의 정사각형 공간 위에 서있다. 이 공간은 1 X 1 크기의 정사각형으로 나누어져 있다.
가장 왼쪽 위 죄표는 (1, 1)이고, 가장 오른쪽 아래 좌표는 (N, N)에 해당한다. 여행가 A는 상하좌우 방향으로 이동할 수 있으며,
시작 좌표는 항상 (1, 1)이다. 여행가 A의 계획서에는 L, R, U, D 중 하나의 문자가 반복적으로 적혀 있다.

    L: 왼쪽으로 한 칸 이동
    R: 오른쪽으로 한 칸 이동
    U: 위쪽으로 한 칸 이동
    D: 아래쪽으로 한 칸 이동

계획서가 주어졌을 때 여행가 A가 최종적으로 도착할 지점의 좌표를 출력하는 프로그램을 작성하시오.

첫째 줄에 공간의 크기를 나타내는 N(1 <= N <= 100)이 주어진다.
둘째 줄에 여행가 A가 이동할 계획서 내용이 주어진다. (1 <= 이동 횟수 <= 100)
'''

n = int(input())
plans = map(int, input().split())
x, y = 1, 1 # 현재 좌표

# L, R, U, D의 따른 이동 방향
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
move = ['L', 'R', 'U', 'D']

# 이동 계획을 하나씩 확인
for plan in plans:
    for i in range(len(move)):
        if plan == move[i]:
            nx = x + dx[i]
            ny = y + dy[i]
            
    # 공간을 벗어나는 경우를 무시
    if nx < 1 or nx > n or ny < 1 or ny > n:
        continue
    
    # 좌표 이동
    x, y = nx, ny
    
print(x, y)