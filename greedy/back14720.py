#우유 축제
N = int(input())
stores = list(map(int, input().split()))

current = 0
r = 0
for n in range(N):
  if stores[n] == current:
    current = (current + 1) % 3
    r+=1
    if current == 3:
      current = 0 
    
print(r)