'''
심술쟁이 해커 임준오(동탄 주민)는 새를 싫어한다. 특히 비둘기를 싫어한다. 준오는 수업시간에 옆자리 짝꿍과 빙고게임을 하기로 했다. 
준오와 짝꿍은 각자 원하는 숫자를 n×m 격자의 빙고판에 적었다. 그러고는 서로의 빙고판을 교환했는데, 준오는 짝꿍의 빙고판을 확인하자마자 화가 치밀어 올랐다. 
짝꿍의 빙고판에 9가 들어간 숫자들이 엄청 많아서 비둘기가 떠올랐기 때문이다. 그래서 준오는 짝꿍의 빙고판을 부숴버렸다.
하지만 준오의 폭동에는 특별한 룰이 있다. 바로 모든 행과 열을 통틀어서 9가 가장 많이 쓰여 있는 행 또는 열을 단 하나만 부수는 것이다!
빙고판을 부수는 순간 준오와 선생님의 눈이 마주쳤고, 선생님은 빙고판에 남아있는 9의 개수만큼 준오를 때리기로 했다. 준오는 몇 대를 맞아야 할까?

첫째 줄에 직사각형 빙고판의 크기를 뜻하는 n(1 ≤ n ≤ 500)과 m(1 ≤ m ≤ 500)이 주어진다. 다음 줄부터 n개의 줄에 걸쳐 각 줄마다 m개의 숫자들이 주어진다. 
이는 크기가 n×m인 짝꿍의 빙고판의 상태를 나타내며, 빙고판에는 10,000 이하의 음이 아닌 정수가 적힌다.
'''

import sys

n, m = map(int, sys.stdin.readline().split())
bingo, row9, column9 = [], [], []

for _ in range(n):
    row9Count = 0
    temp = list(map(str, sys.stdin.readline().split()))
    bingo.append(temp)
    
    for t in temp:
        row9Count += t.count('9')
        
    row9.append(row9Count)
    
for i in range(m):
    column9Count = 0
    
    for j in range(n):
        column9Count += bingo[j][i].count('9')
        
    column9.append(column9Count)
    
print(sum(row9) - max(max(row9), max(column9)))