'''
문제: 시각
정수 N이 입력되면 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함되는
모든 경우의 수를 구하는 프로그램을 작성하시오.

첫째 줄에 정수 N(0 <= N <= 23)을 입력한다.
'''

h = int(input())
count = 0

for i in range(h + 1):
    for j in range(60):
        for k in range(60):
            # i, j, k를 각각 문자열화 하여 문자열에 3이 포함되어 있는지 탐색 
            if '3' in str(i) + str(j) + str(k):
                count += 1
                
print(count)