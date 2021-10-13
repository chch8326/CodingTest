'''
문제: 곱하기 혹은 더하기
각 자리가 숫자 0부터 9로만 이루어진 문자열 S가 주어졌을 때, 왼쪽부터 오른쪽으로 하나씩 모든 숫자를 확인하며 숫자 사이에 곱하기 혹은 더하기 연산자를 넣어
결과적으로 가장 큰 수를 구하는 프로그램을 작성하시오. 단, 더하기보다 곱하기를 먼저 계산하는 일반적인 방식과는 달리 모든 연산은 왼쪽에서부터 순서대로 이루어진다.
'''

s = input()
result = int(s[0])

for i in range(1, len(s)):
    num = int(s[i])
    
    if result <= 1 or num <= 1:
        result += num
    else:
        result *= num
        
print(result)