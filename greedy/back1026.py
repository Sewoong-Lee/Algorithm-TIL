#보물
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()

S = 0
for a in A:
  S += a * max(B)
  B.pop(B.index(max(B)))
print(S)