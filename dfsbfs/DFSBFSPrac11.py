'''
문제: 촌수 계산
우리 나라는 가족 혹은 친척들 사이의 관계를 촌수라는 단위로 표현하는 독특한 문화를 가지고 있다. 이러한 촌수는 다음과 같은 방식으로 계산된다. 
기본적으로 부모와 자식 사이를 1촌으로 정의하고 이로부터 사람들 간의 촌수를 계산한다.
여러 사람들에 대한 부모 자식들 간의 관계가 주어졌을 때, 주어진 두 사람의 촌수를 계산하는 프로그램을 작성하시오.

사람들은 1, 2, 3, …, n (1 ≤ n ≤ 100)의 연속된 번호로 각각 표시된다. 
입력 파일의 첫째 줄에는 전체 사람의 수 n이 주어지고,
둘째 줄에는 촌수를 계산해야 하는 서로 다른 두 사람의 번호가 주어진다. 
셋째 줄에는 부모 자식들 간의 관계의 개수 m이 주어진다. 
넷째 줄부터는 부모 자식간의 관계를 나타내는 두 번호 x,y가 각 줄에 나온다. 이때 앞에 나오는 번호 x는 뒤에 나오는 정수 y의 부모 번호를 나타낸다.
'''

from collections import deque
import sys

n = int(input())
p1, p2 = map(int, input().split())
r = int(input())

graph = [[] * n for _ in range(n + 1)]
visited = [False] * (n + 1)
result = [0] * (n + 1)

for _ in range(r):
    p, c = map(int, sys.stdin.readline().rstrip().split())
    graph[p].append(c)
    graph[c].append(p)
    
def bfs(start):
    queue = deque()
    queue.append(start)
    visited[start] = True
    
    while queue:
        s = queue.popleft()
        
        for i in graph[s]:
            if not visited[i]:
                result[i] = result[s] + 1
                visited[i] = True
                queue.append(i)
                
bfs(p1)

if result[p2] != 0:
    print(result[p2])
else:
    print(-1)