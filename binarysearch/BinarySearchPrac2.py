'''
문제: 떡볶이 떡 만들기
오늘은 떡볶이 떡을 만드는 날이다. 동빈이네 떡볶이 떡은 길이가 일정하지 않다. 대신에 한 봉지 안에 들어가는 떡의 총 길이는 절단기로 잘라서 맞춰준다.
절단기에 높이를 지정하면 줄지어진 떡을 한 번에 절단한다. 높이가 H보다 긴 떡은 H 위의 부분이 잘릴 것이고, 낮은 떡은 짤리지 않을 것이다.
손님이 왔을 때 요청한 총 길이가 M일 때 적어도 M만큼의 떡을 얻기 위해 절단기에 설정할 수 있는 높이의 최대값을 구하는 프로그램을 작성하시오.

첫째 줄에 떡의 개수 N(1 <= N <= 1,000,000)과 요청한 떡의 길이 M(1 <= M <= 2,000,000,000)이 주어진다.
둘째 줄에는 떡의 개별 높이가 주어진다. 떡 높이의 총합은 항상 M 이상이므로, 손님은 필요한 양만큼 떡을 시킬 수 있다. 
높이는 10억보다 작거나 같은 양의 정수이다.
'''

n, m = map(int, input().split())
arr = list(map(int, input().split()))

start = 0
end = max(arr)
result = 0

while start <= end:
    total = 0
    mid = (start + end) // 2
    
    for x in arr:
        if x > mid:
            total += x - mid
            
    if total < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1
        
print(result)
        