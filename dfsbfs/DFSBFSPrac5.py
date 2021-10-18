'''
문제: 경쟁적 전염
N X M 크기의 시험관이 있다. 이 시험관은 1 X 1 크기의 칸으로 나눠지며, 특정한 위치에는 바이러스가 존재할 수 있다.
바이러스의 종류는 1 ~ K번까지 K가지가 있으며 모든 바이러스는 이 중 하나에 속한다. 시허관에 존재하는 모든 바이러스는
1초마다 상, 하, 좌, 우의 방향으로 증식하는데 매초 번호가 낮은 종류의 바이러스부터 먼저 증식한다. 또한 증식 과정에서
특정한 칸에 이미 어떠한 바이러스가 있다면 그곳에는 다른 바이러스가 들어갈 수 없다.
시험관의 크기와 바이러스의 위치 정보가 주어졌을 때, S초가 지난 후에 (X, Y)에 존재하는 바이러스의 종류를 출력하는 프로그램을 작성하시오.
만약 S초가 지난 후에 해당 위치에 바이러스가 존재하지 않는다면 0을 출력한다.

첫째 줄에 자연수 n(1 <= n <= 200), k(1 <= k <= 1,000)가 주어지며, 각 자연수는 공백으로 구분한다.
둘째 줄부터 n개의 줄에 걸쳐서 시험관의 정보가 주어진다. 각 행은 n개의 원소로 구성되며, 해당 위치에 존재하는 바이러스의 번호가
주어지며 공백으로 구분한다. 마지막 줄에는 s(초), x(행), y(열)이 주어지며 공백으로 구분한다.
'''

from collections import deque

n, k = map(int, input().split())
graph = [] # 전체 보드 정보를 담는 리스트
data = [] # 바이러스에 대한 정보를 담는 리스트

for i in range(n):
    graph.append(list(map(int, input().split())))
    
    for j in range(n):
        if graph[i][j] != 0:
            data.append((graph[i][j], 0, i, j)) # 바이러스 종류, 시간(초), 행, 열
            
data.sort() # 낮은 번호의 바이러스가 먼저 증식하므로 오름차순으로 정렬
queue = deque(data)

target_s, target_x, target_y = map(int, input().split())

# 바이러스 증식 방향(상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while queue:
    virus, s, x, y = queue.popleft()
    
    if s == target_s:
        break
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        # 해당 위치로 이동할 수 있는 경우
        if nx >= 0 and nx < n and ny >= 0 and ny < n:
            # 바이러스가 증식되지 않았다면 해당하는 바이러스 종류를 증식
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                queue.append((virus, s + 1, nx, ny))
                
print(graph[target_x - 1][target_y - 1])