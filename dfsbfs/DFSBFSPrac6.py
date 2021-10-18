'''
문제: 연산자 끼워 넣기
N개의 수로 이루어진 수열과 수열의 수와 수 사이에 끼워 넣을 수 있는 N - 1개의 연산자가 주어진다. 연산자는 덧셈, 뺄셈, 곱셈, 나눗셈으로만 이루어져 있다.
우리는 수와 수 사이에 연산자를 하나씩 넣어서 수식을 하나 만들 수 있는데 이때 주어진 수의 순서를 바꾸면 안된다. 식의 계산은 연산자 우선순위를 무시하고
앞에서부터 진행한다. 나눗셈은 정수 나눗셈으로 몫만 취하며, 음수를 양수로 나눌 때는 양수로 바꾼 뒤 몫을 취하고, 그 몫을 음수로 바꾼다.
이렇게 N개의 수와 N - 1개의 연산자가 주어졌을 때 만들 수 있는 식의 결과가 최대인 것과 최소인 것을 구하는 프로그램을 작성하시오.

첫째 줄에 수의 개수 N(2 <= N <= 11)이 주어진다.
둘째 줄에는 수열이 주어진다. (1 <= Ai <= 100)
셋째 줄에는 합이 N - 1인 4개의 정수가 주어지는데 차례대로 덧셈의 개수, 뺄셈의 개수, 곱셈의 개수, 나눗셈의 개수이다.
'''

n = int(input())
data = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

# 최솟값과 최댓값 초기화
max_value = -1e9
min_value = 1e9

def dfs(i, now):
    global add, sub, mul, div, min_value, max_value
   
    if i == n:
        max_value = max(max_value, now)
        min_value = min(min_value, now)
    else:
        # 각 연산자에 대하여 재귀적으로 수행
        if add > 0:
            add -= 1
            dfs(i + 1, now + data[i])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(i + 1, now - data[i])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(i + 1, now * data[i])
            mul += 1
        if div > 0:
            div -= 1
            dfs(i + 1, int(now / data[i])) # 나눌 때는 나머지를 제거
            div += 1

dfs(1, data[0])

print(max_value)
print(min_value)