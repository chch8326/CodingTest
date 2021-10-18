'''
문제: 음료수 얼려 먹기
N X M 크기의 얼음 틀이 있다. 구멍이 뚫려 있는 부분은 0, 칸막이가 존재하는 부분은 1로 표시된다.
구멍이 뚫려 있는 부분끼리 상, 하, 좌, 우로 붙어 있는 경우 서로 연결되어 있는 것으로 간주한다.
이때 얼음 틀의 모양이 주어졌을 때 생성되는 총 아이스크림의 개수를 구하는 프로그램을 작성하시오.

첫 번째 줄에 얼음 틀의 세로 길이 N(1 <= N <= 1,000)과 가로 길이 M(1 <= M <= 1,000)이 주어진다.
두 번째 줄부터 N + 1번째 줄까지 얼음 틀의 형태가 주어진다. 이때 구멍이 뚫려있는 부분은 0, 그렇지 않은 부분은 1이다.
'''

n, m = map(int, input().split())

graph = []

for i in range(n):
    graph.append(list(map(int, input())))

# dfs로 특정 노드를 방문한 뒤에 연결된 모든 노드들도 방문    
def mold(x, y):
    # 범위에 벗어날 경우 함수를 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    
    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0:
        graph[x][y] = 1 # 방문 처리
        
        # 상, 하, 좌, 우의 위치도 모두 재귀적으로 방문  
        mold(x - 1, y)
        mold(x + 1, y)
        mold(x, y - 1)
        mold(x, y + 1)
        
        return True
    
    return False

result = 0

# 음료수 채우기
for i in range(n):
    for j in range(m):
        if mold(i, j) == True:
            result += 1
            
print(result)