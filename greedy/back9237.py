#이장님 초대
N = int(input())
times = list(map(int, input().split()))
times.sort(reverse=True)
max = 0

for i in range(N):
    days = i + 1 + times[i]
    if days > max:
        max = days
print(max + 1)
