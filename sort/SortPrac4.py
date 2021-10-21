'''
문제: 국영수
학생 N명의 이름과 국어, 영어, 수학 점수가 주어진다. 이때 다음과 같은 조건으로 학생의 성적을 정렬하는 프로그램을 작성하시오.
    1. 국어 점수가 감소하는 순서로
    2. 국어 점수가 같으면 영어 점수가 증가하는 순서로
    3. 국어 점수와 영어 점수가 같으면 수학 점수가 감소하는 순서로
    4. 모든 점수가 같으면 이름이 사전 순으로 증가하는 순서로

첫째 줄에 학생 수 N(1 <= N <= 100,000)이 주어진다.
둘째 줄부터 한 줄에 하나씩 각 학생의 이름, 국어, 영어, 수학 점수가 공백으로 구분해 주어진다.
점수는 1보다 크거나 같고, 100보다 작거나 같은 자연수이다.
'''

n = int(input())
students = []

for _ in range(n):
    input_data = input().split()
    students.append((input_data[0], int(input_data[1]), int(input_data[2]), int(input_data[3])))
    
students.sort(key = lambda element : (-element[1], element[2], -element[3], element[0]))

print(students)

for student in students:
    print(student[0], end= ' ')