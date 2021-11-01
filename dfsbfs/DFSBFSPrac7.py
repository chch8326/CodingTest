'''
문제: DFS와 BFS
그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 
더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 
다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.
'''

from collections import deque
import sys

def dfs(graph, start, visited):
    visited[start] = True
    print(start, end = ' ')
    
    for i in graph[start]:
        if not visited[i]:
            dfs(graph, i, visited)
            
def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    
    while queue:
        now = queue.popleft()
        print(now, end = ' ')
        
        for i in graph[now]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

n, m, v = map(int, input().split())

graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(m):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    graph[x].append(y)
    graph[y].append(x)

for i in range(1, n + 1):
    graph[i].sort()
    
dfs(graph, v, visited)
visited = [False] * (n + 1)
print()
bfs(graph, v, visited)