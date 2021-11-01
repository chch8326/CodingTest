'''
전쟁은 어느덧 전면전이 시작되었다. 결국 전투는 난전이 되었고, 우리 병사와 적국 병사가 섞여 싸우게 되었다. 그러나 당신의 병사들은 하얀 옷을 입고, 
적국의 병사들은 파란옷을 입었기 때문에 서로가 적인지 아군인지는 구분할 수 있다. 문제는, 같은 팀의 병사들은 모이면 모일수록 강해진다는 사실이다.
N명이 뭉쳐있을 때는 N^2의 위력을 낼 수 있다. 과연 지금 난전의 상황에서는 누가 승리할 것인가? 단, 같은 팀의 병사들이 대각선으로만 인접한 경우는 뭉쳐 있다고 보지 않는다.

첫째 줄에는 전쟁터의 가로 크기 N, 세로 크기 M(1 ≤ N, M ≤ 100)이 주어진다. 그 다음 두 번째 줄에서 M+1번째 줄에는 각각 (X, Y)에 있는 
병사들의 옷색이 띄어쓰기 없이 주어진다. 모든 자리에는 병사가 한 명 있다. (B는 파랑, W는 흰색이다.)
'''

import sys
from collections import deque
input = sys.stdin.readline

def bfs(x, y, color):
    count = 1
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx >= 0 and nx < m and ny >= 0 and ny < n:
                if graph[nx][ny] == color and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                    count += 1
                    
    return count

n, m = map(int, input().split())
graph = [list(input()) for _ in range(m)]
visited = [[False] * n for _ in range(m)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

white, blue = 0, 0

for i in range(m):
    for j in range(n):
        if graph[i][j] == 'W' and not visited[i][j]:
            white += bfs(i, j, 'W') ** 2
        elif graph[i][j] == 'B' and not visited[i][j]:
            blue += bfs(i, j, 'B') ** 2

print(white, blue)