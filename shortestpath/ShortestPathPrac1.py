'''
문제: 미래 도시
방문 판매원 A는 많은 회사가 모여 있는 공중 미래 도시에 있다. 공중 미래 도시에는 1번부터 N번까지의 회사가 있는데 특정 회사끼리는 서로 도로를 통해
연결되어 있다. 방문 판매원 A는 현재 1번 회사에 위치해 있으며, X번 회사에 방문해 물건을 판매하고자 한다. 공중 미래 도시에서 특정 회사에 도착하기
위한 방법은 회사끼리 연결되어 있는 도로를 이용하는 방법이 유일하다. 또한 연결된 2개의 회사는 양방향으로 이동할 수 있다. 공중 미래 도시에서의 도로는
마하의 속도로 사람을 이동시켜주기 때문에 특정 회사와 다른 회사가 도로로 연결되어 있다면 정확히 1만큼의 시간으로 이동할 수 있다. 또한 오늘 방문 판매원
A는 기대하던 소개팅에도 참석하고자 한다. 소개팅의 상대는 K번 회사에 있다. 방문 판매원 A는 X번 회사에 가서 물건을 판매하기 전에 먼저 소개팅 상대의
회사에 찾아가서 함께 커피를 마실 예정이다. 따라서 방문 판매원 A는 1번 회사에서 출발하여 K번 회사를 방문한 뒤에 X번 회사로 가는 것이 목표다. 이때
방문 판매원 A는 가능한 한 빠르게 이동하고자 한다. 방문 판매원 A가 회사 사이를 이동하게 되는 최소 시간을 계산하는 프로그램을 작성하시오. 
이때 소개팅의 상대방과 커피를 마시는 시간 등은 고려하지 않는다고 가정한다. 만약 X번 회사에 도달할 수 없다면 -1을 출력한다.

첫째 줄에 전체 회사의 개수 N(1 <= N <= 100)과 경로의 개수 M(1 <= K <= 100)이 공백으로 구분되어 차례대로 주어진다.
둘째 줄부터 M + 1번째 줄에는 연결된 두 회사의 번호가 공백으로 구분되어 주어진다.
M + 2번째 줄에는 X와 K(1 <= K <= 100)가 공백으로 구분되어 차례대로 주어진다.
'''

INF = int(1e9)

n, m = map(int, input().split())
graph = [[INF] * (n + 1) for _ in range(n + 1)]

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0
        
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1
    
k, x = map(int, input().split())

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
            
distance = graph[1][k] + graph[k][x]

if distance >= INF:
    print(-1)
else:
    print(distance)