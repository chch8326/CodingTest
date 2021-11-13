'''
문제: 유니크
상근이와 친구들은 MT에 가서 아래 설명과 같이 재미있는 게임을 할 것이다. 각 플레이어는 1이상 100 이하의 정수를 카드에 적어 제출한다. 
각 플레이어는 자신과 같은 수를 쓴 사람이 없다면, 자신이 쓴 수와 같은 점수를 얻는다. 만약, 같은 수를 쓴 다른 사람이 있는 경우에는 점수를 얻을 수 없다.
상근이와 친구들은 이 게임을 3번 했다. 각 플레이어가 각각 쓴 수가 주어졌을 때, 3번 게임에서 얻은 총 점수를 구하는 프로그램을 작성하시오.

첫째 줄에 참가자의 수 N이 주어진다. (2 ≤ N ≤ 200) 둘째 줄부터 N개 줄에는 각 플레이어가 1번째, 2번째, 3번째 게임에서 쓴 수가 공백으로 구분되어 주어진다.
'''

import sys

n = int(sys.stdin.readline())
first, second, third = [], [], []

for _ in range(n):
    a, b, c = map(int, sys.stdin.readline().split())
    first.append(a)
    second.append(b)
    third.append(c)
    
for i in range(n):
    score = 0
    
    if first.count(first[i]) == 1:
        score += first[i]
        
    if second.count(second[i]) == 1:
        score += second[i]
        
    if third.count(third[i]) == 1:
        score += third[i]
        
    print(score)