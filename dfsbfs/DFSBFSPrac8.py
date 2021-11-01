'''
문제: 미로 탐색
N × M크기의 배열로 표현되는 미로가 있다. 미로에서 1은 이동할 수 있는 칸을 나타내고, 0은 이동할 수 없는 칸을 나타낸다. 이러한 미로가 주어졌을 때, 
(1, 1)에서 출발하여 (N, M)의 위치로 이동할 때 지나야 하는 최소의 칸 수를 구하는 프로그램을 작성하시오. 

첫째 줄에 두 정수 N, M(2 ≤ N, M ≤ 100)이 주어진다. 다음 N개의 줄에는 M개의 정수로 미로가 주어진다. 각각의 수들은 붙어서 입력으로 주어진다.
'''

from collections import deque
import sys

n, m = map(int, input().split())
graph = []

for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().rstrip())))
    
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def miro(x, y):
    queue = deque()
    queue.append((x, y))
    
    while queue:
        next_x, next_y = queue.popleft()
        
        for i in range(4):
            nx = next_x + dx[i]
            ny = next_y + dy[i]
            
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            
            if graph[nx][ny] == 0:
                continue
            
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[next_x][next_y] + 1
                queue.append((nx, ny))
                
    return graph[n - 1][m - 1]

print(miro(0, 0))