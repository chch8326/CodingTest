'''
문제: 단지 번호 붙이기
1은 집이 있는 곳을, 0은 집이 없는 곳을 나타낸다. 철수는 이 지도를 가지고 연결된 집의 모임인 단지를 정의하고, 단지에 번호를 붙이려 한다. 
여기서 연결되었다는 것은 어떤 집이 좌우, 혹은 아래위로 다른 집이 있는 경우를 말한다. 대각선상에 집이 있는 경우는 연결된 것이 아니다.
지도를 입력하여 단지수를 출력하고, 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력하는 프로그램을 작성하시오.

첫 번째 줄에는 지도의 크기 N(정사각형이므로 가로와 세로의 크기는 같으며 5≤N≤25)이 입력되고, 
그 다음 N줄에는 각각 N개의 자료(0혹은 1)가 입력된다.
'''

def dfs(x, y):
    global count
    
    if 0 <= x < n and 0 <= y < n:
        if graph[x][y] == 1 and not visited[x][y]:
            count += 1
            visited[x][y] = True
            
            dfs(x - 1, y)
            dfs(x + 1, y)
            dfs(x, y - 1)
            dfs(x, y + 1)
            
            return True
        
    return False

n = int(input())

graph = [list(map(int, input())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

count, result = 0, 0
arr = []

for i in range(n):
    for j in range(n):
        if dfs(i, j) == True:
            arr.append(count)
            result += 1
            count = 0
            
arr.sort()
print(result)

for i in range(len(arr)):
    print(arr[i])