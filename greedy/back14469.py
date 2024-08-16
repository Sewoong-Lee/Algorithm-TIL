#소가 길을 건너간 이유 3
N = int(input())
times = []
for _ in range(N):
    a, c = map(int, input().split())
    times.append((a, c))

times.sort()

time = 0

for n in range(N):
    a, c = times[n]
    if time < a:
        time = a
    time += c 

print(time)
