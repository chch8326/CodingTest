'''
문제: 로또 추첨
로또 번호는 중복되지 않아야 한다.
'''

import random

# 직접 구현
lotto1 = []

while True:
    if len(lotto1) == 6:
        break
    
    num = random.randint(1, 45)
    
    if num not in lotto1:
        lotto1.append(num)
        
lotto1.sort()

for num in lotto1:
    print(num, end = ' ')
    
print()

# set을 이용하여 중복 제거
data = set()

while True:
    if len(data) == 6:
        break
    
    data.add(random.randint(1, 45))
    
lotto2 = sorted(list(data))

for num in lotto2:
    print(num, end = ' ')