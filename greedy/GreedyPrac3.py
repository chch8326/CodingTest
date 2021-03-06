'''
문제: 문자열 뒤집기
0과 1로만 이루어진 문자열 S가 있다. 이 문자열 S에 있는 모든 숫자를 전부 같게 만들려고 한다. 모든 숫자를 전부 같게 만드는 방법은
방법은 문자열 S에서 연속된 하나 이상의 숫자를 잡고 모두 뒤집는 것이다. 뒤집은 것은 0을 1로, 1을 0으로 뒤집는 것이다.
문자열 S가 주어졌을 때, 문자열을 뒤집는 최소 횟수를 출력하는 프로그램을 작성하시오.
'''

s = input()
count0 = 0 # 전부 0으로 바꾸는 경우
count1 = 0 # 전부 1로 바꾸는 경우

# 첫번 째 요소 처리
if s[0] == '1':
    count0 += 1
else:
    count1 += 1
    
for i in range(len(s) - 1):
    if s[i] != s[i + 1]:
        # 다음 수에서 1로 바뀌는 경우
        if[i + 1] == '1':
            count0 += 1
        # 다음 수에서 0으로 바뀌는 경우    
        else:
            count1 += 1
            
print(min(count0, count1))