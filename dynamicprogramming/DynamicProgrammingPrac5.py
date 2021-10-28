'''
문제: 못생긴 수
몽생긴 수란 오직 2, 3, 5만을 소인수로 가지는 수를 의미한다. 다시 말해 오직 2, 3, 5를 약수로 가지는 합성수를 의미한다.
1은 못생긴 수라고 가정한다. 이때 n번째 못생긴 수를 찾는 프로그램을 작성하시오.

첫째 줄에 n(1 <= n <= 1,000)이 입력된다.
'''

n = int(input())

ugly = [0] * n
ugly[0] = 1

i2 = i3 = i5 = 0
next2, next3, next5 = 2, 3, 5

for k in range(1, n):
    ugly[k] = min(next2, next3, next5)
    
    if ugly[k] == next2:
        i2 += 1
        next2 = ugly[i2] * 2
        
    if ugly[k] == next3:
        i3 += 1
        next3 = ugly[i3] * 3
        
    if ugly[k] == next5:
        i5 += 1
        next5 = ugly[i5] * 5
        
print(ugly[n - 1])