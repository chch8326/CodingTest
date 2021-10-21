'''
문제: 위에서 아래로
하나의 수열에는 다양한 수가 존재한다. 이러한 수는 크기에 상관없이 나열되어 있다. 이 수를 큰 수 부터 작은 수의 순서로 정렬해야 한다.
수열을 내림차순으로 정렬하는 프로그램을 만드시오.

첫째 줄에 수열에 속해 있는 수의 개수 N(1 <= N <= 500)이 주어진다.
둘째 줄부터 N + 1번째 줄까지 N개의 수가 입력된다. 수열의 범위는 1 이상 100,000 이하의 자연수이다.
'''

n = int(input())
arr = []

for i in range(n):
    arr.append(int(input()))
    
result = sorted(arr, reverse = True)

for i in result:
    print(i, end = ' ')