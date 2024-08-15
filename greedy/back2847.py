#게임을 만든 동준이N = int(input())
N = int(input())
levels = []
for _ in range(N):
  l = int(input())
  levels.append(l)

c = 0;

for i in range(N-1, 0, -1):
  if levels[i] <= levels[i-1]:
      dif = levels[i-1] - levels[i] + 1
      levels[i-1] -= dif  
      c += dif
      
print(c)