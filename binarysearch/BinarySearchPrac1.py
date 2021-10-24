'''
문제: 부품 찾기
전자 매장에 부품이 N개 있다. 각 부품은 정수 형태의 고유한 번호가 있다. 어느 날 손님이 M개 종류의 부품을 대량으로 구매하겠다며
당일 날 견적서를 요청했다. 손님이 문의한 부품 M개 종류를 모두 확인해서 견적서를 작성해야 한다. 이때 가게 안에 부품이 모두 있는지
확인하는 프로그램을 작성하시오. 이때 손님이 요청한 부품 번호의 순서대로 부품을 확인해 부품이 있으면 yes를 없으면 no를 출력한다.

첫째 줄에 정수 N(1 <= N <= 1,000,000)이 주어진다.
둘째 줄에는 공백으로 구분하여 N개의 정수가 주어진다. 이때 정수는 1보다 크고 1,000,000 이하이다.
셋째 줄에는 정수 M(1 <= M <= 100,000)이 주어진다.
넷째 줄에는 공백으로 구분하여 M개의 정수가 주어진다. 이때 정수는 1보다 크고 1,000,000 이하이다.
'''

def binary_search(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
            
    return None

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
m = int(input())
x = list(map(int, input().split()))

for i in x:
    result = binary_search(arr, i, 0, n - 1)
    
    if result != None:
        print('yes', end = ' ')
    else:
        print('no', end = ' ')
        
'''
집합 자료형 이용

n = int(input())
arr = set(map(int, input().split()))
m = int(input())
x = list(map(int, input().split()))

for i in x:
    if i in arr:
        print('yes', end = ' ')
    else:
        print('no', end = ' ')
'''