'''
문제: 성적이 낮은 순서로 학생 출력하기
N명의 학생 정보가 있다. 학생 정보는 학생의 이름과 성적으로 구분된다. 각 학생의 이름과 성적 정보가
주어졌을 때 성적이 낮은 순서대로 학생의 이름을 출력하는 프로그램을 작성하시오.

첫 번째 줄에 학생의 수 N(1 <= N <= 100,000)이 입력된다.
두 번째 줄부터 N + 1번째 줄에는 학생의 이름을 나타내는 문자열 A와 학생의 성적을 나타내는 정수 B가 공백으로 구분되어 입력된다.
문자열 A의 길이와 학생의 성적은 100 이하의 자연수이다.
'''

n = int(input())
arr = []

for i in range(n):
    input_data = input().split()
    arr.append((input_data[0], int(input_data[1])))
    
result = sorted(arr, key = lambda student : student[1])

for student in result:
    print(student[0], end = ' ')