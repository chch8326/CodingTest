'''
문제: 문자열 재정렬
알파벳 대문자와 숫자(0 ~ 9)로만 구성된 문자열이 입력으로 주어진다. 이때 모든 알파벳을 오름차순으로 정렬하여
이어서 출력한 뒤에 모든 숫자를 더한 값을 뒤에 출력하는 프로그램을 작성하시오.

첫째 줄에 하나의 문자열 S(1 <= S의 길이 <= 10,000)가 주어진다.
'''

s = input()
result = []
value = 0

for e in s:
    if e.isalpha(): # 알파벳인지 확인, 알파벳이 맞다면 리스트에 삽입
        result.append(e)
    else: # 알파벳이 아니면 더해둠
        value += int(e)
        
result.sort() # 리스트에 삽입된 알파벳들을 정렬

# 입력된 문자열에 숫자가 있었다면 0보다 커야함
if value != 0:
    result.append(str(value))
    
print(''.join(result))