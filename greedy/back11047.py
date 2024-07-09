#동전 0
N, K = map(int, input().split())
coins = []
for n in range(N):
  i = int(input())
  coins.append(i)
coins.sort(reverse=True)
r=0
for coin in coins:
 if K != 0:
     r += K//coin
     K %= coin
print(r)