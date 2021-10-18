'''
문제: 특정 거리의 도시 찾기
어떤 나라에는 1 ~ N번까지의 도시와 M개의 단방향 도로가 존재한다. 모든 도로의 거리는 1이다. 이때 특정한 도시 X로부터 출발하여
도달할 수 있는 모든 도시 중에서 최단 거리가 K인 모든 도시의 번호를 출력하는 프로그램을 작성하시오.
출발 도시 X에서 출발 도시 X로 가는 최단 거리는 항상 0이라고 가정한다.

첫째 줄에 도시의 개수 N(2 <= N <= 300,000), 도로의 개수 M(1 <= M <= 1,000,000), 
거리 정보 K(1 <= K <= 3,00,000), 출발 도시의 번호 X(1 <= X <= N)가 주어진다.
둘째 줄부터 M개의 줄에 걸쳐서 두 개의 자연수 A, B가 주어지며, 각 자연수는 공백으로 구분한다.
A, B란 A번 도시에서 B번 도시로 이동하는 단방향 도로가 존재한다는 의미이다.

X로부터 출발하여 도달할 수 있는 도시 중에서 최단 거리가 K인 모든 도시의 번호를 한 줄에 하나씩 오름차순으로 출력한다.
이때 도달할 수 있는 도시 중에서 최단 거리가 K인 도시가 하나도 존재하지 않으면 -1을 출력한다.
'''

from collections import deque

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)] # 0부터 n까지의 리스트 생성

# 모든 도로 정보 입력
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

# 최단 거리 정보    
distance = [-1] * (n + 1) # 모든 도시에 대한 최단 거리 정보 초기화
distance[x] = 0 # 출발 도시까지의 거리는 0으로 설정

queue = deque([x])

while queue:
    now = queue.popleft()
    
    # 현재 도시에서 이동할 수 있는 모든 도시를 확인
    for next_node in graph[now]:
        # 아직 방문하지 않은 도시라면
        if distance[next_node] == -1:
            distance[next_node] = distance[now] + 1 # 최단 거리 갱신
            queue.append(next_node)
            
check = False
            
# 최단 거리가 K인 모든 도시의 번호를 오름차순으로 출력
for i in range(1, n + 1):
    if distance[i] == k:
        print(i, end = ' ')
        check = True
        
# 만약 최단 거리가 K인 도시가 없다면, -1 출력
if check == False:
    print(-1)