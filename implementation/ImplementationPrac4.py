'''
문제: 럭키 스트레이트
한 게임의 캐릭터는 필살기인 럭키 스트레이트 기술이 있다. 이 기술은 게임 내에서 점수가 특정 조건을 만족할 때만 사용할 수 있다.
현재 캐릭터의 점수를 N이라고 할 때 자릿수를 기주느로 점수 N을 반으로 나누어 왼쪽 부분의 각 자릿수의 합과 오른쪽 부분의 각 자릿수의 합을
더한 값이 동일할 때만 럭키 스트레이트 기술을 사용할 수 있다.
현재 점수 N이 주어지면 럭키 스트레이트를 사용할 수 있는 상태인지 아닌지를 알려주는 프로그램을 작성하시오.

첫째 줄에 N(1 <= N <= 99,999,999)이 정수로 주어진다. 단, 점수 N의 자릿수는 항상 짝수 형태로만 주어진다.
'''

n = input()
standard = len(n)

if standard % 2 == 0:
    left = 0
    right = 0
    
    for i in range(standard // 2):
        left += int(n[i])
        
    for i in range((standard // 2), standard):
        right += int(n[i])
        
    if left == right:
        print('LUCKY STRATE')
    else:
        print('READY')