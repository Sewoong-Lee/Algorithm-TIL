#스네이크버드
N, L = map(int, input().split())
H = list(map(int, input().split()))
H.sort()
for h in H:
  if h <= L:
    L += 1
print(L)