'''
문제: 안테나
일직선상의 마을에 여러 채의 집이 위치해 있다. 이 중에서 특정 위치의 집에 특별히 한 개의 안테나를 설치하기로 결정했다.
효율성을 위해 안테나로부터 모든 집까지의 거리의 총합이 최소가 되도록 설치하려고 한다. 이때 안테나는 집이 위치한 곳에만
설치할 수 있고, 논리적으로 한 위치에 여러 개의 집이 존재하는 것이 가능하다.
집들의 위치 값이 주어질 때 안테나를 설치할 위치를 선택하는 프로그램을 작성하시오.

첫째 줄에 집의 수 N(1 <= N <= 200,000)이 자연수로 주어진다.
둘째 줄에 N채의 집에 위치가 공배으로 구분되어 1 이상 100,000 이하의 자연수로 주어진다.
'''

n = input()
home = list(map(int, input().split()))
home.sort()

# "효율성을 위해 안테나로부터 모든 집까지의 거리의 총합이 최소가 되도록 설치"
# 이 말은 즉슨 가운데 값을 구하라는 것을 의미한다.
print(home[(n - 1) // 2])