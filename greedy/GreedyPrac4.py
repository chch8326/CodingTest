'''
문제: 만들 수 없는 금액
N개의 동전을 이용하여 만들 수 없는 양의 정수 금액 중 최솟값을 구하는 프로그램을 작성하시오.

첫째 줄에는 동전의 개수를 나타내는 양의 정수 N(1 <= N <= 1,000)이 주어진다.
둘째 줄에는 각 동전의 화폐 단위를 나타내는 N개의 자연수가 주어지며, 각 자연수는 공백으로 구분한다.
'''

n = int(input())
coins = list(map(int, input().split()))
coins.sort()

target = 1

for x in coins:
    if target < x:
        break
    
    target += x
    
print(target)