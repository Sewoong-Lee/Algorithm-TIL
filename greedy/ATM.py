# ATM
N = int(input())
times = list(map(int, input().split()))

times.sort()
result = 0 # 인출 완료까지 총 시간
cumTime = 0 # 인당 인출 시간

for time in times:
    cumTime += time
    result += cumTime
    
print(result)
