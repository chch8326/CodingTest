'''
문제: 미로 탈출
N X M 크기의 직사각형 형태의 미로에는 여러 마리의 괴물들이 있어 이를 피해 탈출해야 한다. 캐릭터의 위치는 (1, 1)이고
미로의 출구는 (N, M) 위치에 존재하며 한 번에 한 칸씩 이동할 수 있다. 이때 괴물이 있는 부분은 0으로 괴물이 없는 부분은 1로 표시된다.
캐릭터가 미로를 탈출하기 위해 움직이여야 하는 최소 칸의 개수를 구하는 프로그램을 작성하시오.

첫째 줄에 두 정수 N(4 <= N <= 200), M(4 <= M <= 200)이 주어진다. 다음 N개의 줄에는 각각 M개의 정수 (0 혹은 1)로
미로의 정보가 주어진다. 각각의 수들은 공백 없이 붙어서 입력으로 제시된다. 시작 칸과 마지막 칸은 항상 1이어야 한다.    
'''
from collections import deque

n, m = map(int, input().split())

graph = []

for i in range(n):
    graph.append(list(map(int, input())))
    
# 캐릭터가 이동할 방향 정의(상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0 , -1, 1]

def miro(x, y):
    queue = deque()
    queue.append((x, y))
    
    # queue가 빌 때까지 반복
    while queue:
        x, y = queue.popleft()
        
        # 현재 위치에서 네 방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 범위에서 벗어나는 경우를 방지
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            
            # 몬스터가 위치하는 곳을 피함
            if graph[nx][ny] == 0:
                continue
            
            # 해당 노드를 처음 방문하는 경우에만 최단거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
                
    return graph[n - 1][m - 1]

print(miro(0, 0))
print(graph)