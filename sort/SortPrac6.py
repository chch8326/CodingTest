'''
문제: 실패율
슈퍼 게임 개발자 오렐리는 큰 고민에 빠졌습니다. 그녀가 만든 프렌즈 오천성이 대성공을 거뒀지만 요즘 신규 사용자의 수가 급감했습니다.
원인은 신규 사용자 사이에 스테이지 차이가 너무 큰 것이 문제였습니다. 이 문제를 어떻게 할까 고민한 그녀는 동적으로 게임 시간을 늘려서
난이도를 조절하기로 했습니다. 역시 슈퍼 개발자라 대두분의 로직은 쉽게 개발했지만 실패율을 구하는 부분에서 위기에 빠지고 말았습니다.

    실패율 = 스테이지에 도달했으나 아직 클리어하지 못한 플레이어 수 / 스테이지에 도달한 플레이어의 수
    
전체 스테이지의 개수 N, 게임을 이용하는 사용자가 현재 멈춰있는 스테이지의 번호가 담긴 배열 stages가 매개변수로 주어질 때
실패율이 높은 스테이지부터 내림차순으로 스테이지의 번호가 담겨 있는 배열을 return하도록 solution 함수를 완성하시오.
'''

n = int(input())
stages = list(map(int, input().split()))

def solution(n, stages):
    answer = []
    length = len(stages)
    
    for i in range(n):
        length -= stages.count(i)
        fail = stages.count(i + 1) / length
        answer.append((i + 1, fail))
        
    answer = sorted(answer, key = lambda element : element[1], reverse = True)
    answer = [i[0] for i in answer]
    return answer

print(solution(n, stages))