'''
문제: 연구소
인체에 치명적인 바이러스를 연구하던 연구소에서 바이러스가 유출되었다. 다행히 바이러스는 아직 퍼지지 않았고, 바이러스 확산을 막기 위해서 연구소에 벽을 세우려 한다.
연구소 크기가 N X M이며, 1 X 1 크기의 정사각형으로 나누어져 있다. 연구소는 빈 칸, 벽으로 이루어져 있으며, 벽은 칸 하나를 차지한다.
일부 칸은 바이러스가 존재하며, 이 바이러스는 상하좌우로 인접한 빈칸으로 모두 퍼져나갈 수 있다. 바이러스를 막기 위해 새로 세울 수 있는 벽의 개수는 3개이다.

0: 빈칸    1: 벽    2: 바이러스
아무런 벽을 세우지 않는다면 바이러스는 모두 빈 칸으로 퍼져나갈 수 있다. 벽을 3개 세운 뒤 바이러스가 퍼질 수 없는 곳을 안전 영역이라고 할 때
주어진 연구소의 크기에서 안전 영역 크기의 최댓값을 구하는 프로그램을 작성하시오.

첫째 줄에 지도의 세로 크기 N(3 <= N <= 8)과 가로 크기 M(3 <= M <= 8)이 주어진다.
둘째 줄에는 연구소 지도가 주어지고, 바이러스의 개수는 2 ~ 10개까지이다.
'''

n, m = map(int, input().split())
lab = [] # 초기 맵 리스트
temp = [[0] * m for _ in range(n)] # 벽을 설치한 뒤의 맵 리스트

for _ in range(n):
    lab.append(list(map(int, input().split())))

# 4개의 방향 이동 (상, 하, 좌, 우)    
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

result = 0

# dfs를 이용한 바이러스 전파
def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        # 바이러스가 퍼질 수 있는 경우
        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                virus(nx, ny)
                
# 현재 맵에서 안전 영역의 개수 계산
def getSafeZone():
    safeZone = 0
    
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                safeZone += 1
                
    return safeZone

# dfs를 이용해 벽을 설치하면서, 매 번 안전 영역의 개수 계산
def dfs(count):
    global result
    
    # 벽이 3개일 경우
    if count == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = lab[i][j]
                
        # 각각의 바이러스 위치에서 전파 진행
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i, j)
                    
        result = max(result, getSafeZone())
        return
    
    # 빈 공간에 벽 설치
    for i in range(n):
        for j in range(m):
            if lab[i][j] == 0:
                lab[i][j] = 1
                count += 1
                dfs(count)
                lab[i][j] = 0
                count -= 1
                
dfs(0)
print(result)
print(temp)
